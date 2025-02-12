# router/product_type.py
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc

from database import SessionLocal, engine
from model import CategoryModel
from schema import CategorySchema

# สร้าง APIRouter สำหรับหมวดหมู่สินค้า
router = APIRouter(
    prefix = "/category",
    tags = ["category"],
)

@router.get("/")
def list_category(category_status: str = '', limit: int = 10, page: int = 1, q: str = ''):
    session = SessionLocal()
        
    offset = (page * limit) - limit; 

    try:

        query = session.query(CategorySchema).filter(CategorySchema.status != 'remove')

        if category_status:
            query = query.filter(CategorySchema.status == category_status)

        if q:
            query = query.filter(CategorySchema.name.ilike(f'%{q}%'))
            
        # ถ้ามี category_status จะไม่ใช้ limit และ offset
        if category_status:
            categorys = query.order_by(desc(CategorySchema.id)).all()
        else:
            # ถ้าไม่มี category_status ใช้ limit และ offset
            categorys = query.order_by(desc(CategorySchema.id)).limit(limit).offset(offset).all()

        total = query.count()

        return {
            "message": "Get all category",
            "rows": [{"id": category.id, "name": category.name, "status": category.status} for category in categorys],
            "total": total
        }
    finally:
        session.close()

# ดึงข้อมูลตามไอดีจากตาราง tb_category
@router.get("/{category_id}")
def get_category(category_id: int = ''):
    session = SessionLocal()
    try:
        category = session.query(CategorySchema).filter(CategorySchema.id == category_id).first()
        if not category:
            raise HTTPException(status_code=404, detail="ไม่พบข้อมูลหมวดหมู่สินค้า")
        return {
            "message": "Get category by ID",
            "row": {"id": category.id, "name": category.name, "status": category.status}
        }
    finally:
        session.close()

# API สำหรับเพิ่มข้อมูลหมวดหมู่สินค้า
@router.post("/")
async def add_category(category: CategoryModel):
    session = SessionLocal()
    try:
        
        new_category = CategorySchema(
            name=category.name,
            status=category.status,
        )
        session.add(new_category)
        session.commit()  
        session.refresh(new_category)

        return {
            "success": True,
            "message": "บันทึกข้อมูลสินค้าสำเร็จ",
            "updated_data": new_category
        }
    finally:
        session.close()

# API สำหรับอัปเดทข้อมูลหมวดหมู่สินค้า
@router.put("/{category_id}")
def update_category(category_id: int, category: CategoryModel):
    session: Session = SessionLocal()
    try:
        existing_category = session.query(CategorySchema).filter(CategorySchema.id == category_id).first()

        if not existing_category:
            raise HTTPException(status_code=404, detail="ไม่พบข้อมูลหมวดหมู่สินค้า")

        if category.name is not None:
            existing_category.name = category.name
        if category.status is not None:
            existing_category.status = category.status

        updated_fields = {} 
        updated_fields = existing_category
        session.commit()

        return {
            "success": True,
            "message": "เเก้ไขข้อมูลสำเร็จ!",
            "id": category_id,
            "updated_data": updated_fields  
        }
    finally:
        session.close()

@router.delete("/{category_id}")
def remove_category(category_id: int):
    session: Session = SessionLocal()  # สร้าง session ใหม่

    try:
        # ค้นหาสินค้าจาก product_id
        existing_category = session.query(CategorySchema).filter(CategorySchema.id == category_id).first()

        # เปลี่ยนสถานะสินค้าเป็น remove
        existing_category.status = "remove"

        # บันทึกการเปลี่ยนแปลง
        session.commit()

        # อัปเดตข้อมูลสินค้าและส่งกลับ
        session.refresh(existing_category)

        return {
            "success": True,
            "message": "อัปเดตสถานะหมวดหมู่สินค้าเป็น remove สำเร็จ",
            "updated_data": existing_category
        }

    finally:
        session.close()  # ปิด session
