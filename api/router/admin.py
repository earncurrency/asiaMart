from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc

from database import SessionLocal, engine
from model import AdminModel
from schema import AdminSchema

# สร้าง APIRouter สำหรับหมวดหมู่สินค้า
router = APIRouter(
    prefix = "/admins",
    tags = ["admins"],
)

#เเสดง admin ทั้งหมด
@router.get("/")
def list_admins(page: int = 1, limit: int = 10, status: str = '', q: str = ''):
    session = SessionLocal()
        
    offset = (page * limit) - limit; 

    try:
        # คำนวณ offset จาก page และ limit
        offset = (page * limit) - limit; 

        query = session.query(AdminSchema).filter(AdminSchema.status != 'remove')

        if status:
            query = query.filter(AdminSchema.status == status)

        if q:
            query = query.filter(AdminSchema.name.ilike(f'%{q}%'))

        admins = query.order_by(desc(AdminSchema.id)).limit(limit).offset(offset).all()

        total = query.count()

        return {
            "message": "Get admins successfully",
            "rows": [
                {
                    "id": a.id,
                    "code": a.code,
                    "name": a.name,
                    "phone": a.phone,
                    "status": a.status,
                } for a in admins
            ],
            "total": total
        }
    finally:
        session.close()

#เเสดง admin ตาม admin_id
@router.get("/{admin_id}")
def get_admin(admin_id: int):
    session = SessionLocal()
    try:

        query = session.query(AdminSchema).filter(AdminSchema.id == admin_id)
        admin = query.first()

        if not admin:
            raise HTTPException(status_code=404, detail="ไม่พบข้อมูลพนักงานในระบบ")

        return {
            "message": "Get admin successfully",
            "row": {
                    "id": admin.id,
                    "code": admin.code,
                    "name": admin.name,
                    "phone": admin.phone,
                    "status": admin.status,
                } 
        }
    finally:
        session.close()

@router.post("/")
async def add_admin(admin: AdminModel):
    session = SessionLocal()
    try:
        
        new_admin = AdminSchema(
            code=admin.code,
            name=admin.name,
            phone=admin.phone,
            status=admin.status,
        )
        session.add(new_admin)
        session.commit()  
        session.refresh(new_admin)

        return {
            "success": True,
            "message": "บันทึกข้อมูลสำเร็จ",
            "updated_data": new_admin
        }
    finally:
        session.close()

#update ตาม admin_id
@router.put("/{admin_id}")
def update_admin(admin_id: int, admin: AdminModel):
    session: Session = SessionLocal()
    try:
        existing_admin = session.query(AdminSchema).filter(AdminSchema.id == admin_id).first()

        if not existing_admin:
            raise HTTPException(status_code=404, detail="ไม่พบข้อมูล")

        if admin.code is not None:
            existing_admin.code = admin.code
        if admin.name is not None:
            existing_admin.name = admin.name
        if admin.phone is not None:
            existing_admin.phone = admin.phone
        if admin.status is not None:
            existing_admin.status = admin.status

        updated_fields = {} 
        updated_fields = existing_admin
        session.commit()

        return {
            "success": True,
            "message": "เเก้ไขข้อมูลสำเร็จ!",
            "id": admin_id,
            "updated_data": updated_fields  
        }
    finally:
        session.close()

@router.post("/login")
async def login(admin: AdminModel):
    session = SessionLocal()

    try:
        query = session.query(AdminSchema).filter(AdminSchema.code == admin.code)
        admin = query.first()  

        if admin is None:
            return {
                "success": False,  
                "message": "ไม่พบข้อมูลพนักงานในระบบ"  
            }

        # ถ้าพบ admin
        return {
            "success": True,
            "admin_name": admin.name,  
            # "admin_role": "admin",  
            "message": "เข้าสู่ระบบสำเร็จ"  
        }
    finally:
        session.close() 