# router/member.py
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc

from database import SessionLocal, engine
from model import MemberModel 
from schema import MemberSchema 

# สร้าง APIRouter สำหรับสมาชิก
router = APIRouter(
    prefix = "/members",
    tags = ["members"],
)

# ดึงข้อมูลทั้งหมดจากตาราง tb_member
@router.get("/")
def get_members(limit: int = 10 , q: str = '', page: int = 1):
    session = SessionLocal()

    offset = (page * limit) - limit; 

    try:

        query = session.query(MemberSchema)

        if q:
            query = query.filter(MemberSchema.name.ilike(f'%{q}%'))

        members = query.order_by(desc(MemberSchema.id)).limit(limit).offset(offset).all()    

        total = query.count()
        
        return {
            "message": "Get all members",
            "rows": [{"id": member.id, "code": member.code, "name": member.name, "phone": member.phone, "status": member.status} for member in members],
            "total": total
        }
    finally:
        session.close()

# ดึงข้อมูลตามไอดีจากตาราง tb_member
@router.get("/{member_id}")
def get_member(member_id: int):
    session = SessionLocal()
    try:
        member = session.query(MemberSchema).filter(MemberSchema.id == member_id).first()
        if not member:
            raise HTTPException(status_code=404, detail="ไม่พบข้อมูลสมาชิก")
        return {
            "message": "Get member by ID",
            "row": {"id": member.id, "code": member.code, "name": member.name, "phone": member.phone, "status": member.status}
        }
    finally:
        session.close()

# เพิ่มข้อมูลสมาชิก
@router.post("/")
def add_member(member: MemberModel):
    session = SessionLocal()
    try:
        # ตรวจสอบว่า member.code มีอยู่ในฐานข้อมูลแล้วหรือยัง
        existing_member = session.query(MemberSchema).filter_by(code=member.code).first()

        if existing_member:
            # ถ้ามีแล้วก็ไม่ต้องเพิ่ม
            return {"message": "สมาชิกนี้มีอยู่แล้ว", "id": existing_member.id}
        
        # ถ้ายังไม่มีสมาชิกที่ตรงกับ member.code ให้เพิ่มสมาชิกใหม่
        new_member = MemberSchema(
            code=member.code,
            name=member.name,
            status=member.status,
        )

        # เพิ่มสมาชิกใหม่ลงในฐานข้อมูล
        session.add(new_member)
        session.commit()

        # ส่งคืนข้อความการเพิ่มข้อมูลสำเร็จ
        return {"message": "เพิ่มสมาชิกสำเร็จ", "id": new_member.id}
    finally:
        session.close()

# API สำหรับอัปเดทข้อมูลสมาชิก
@router.put("/{member_id}")
def update_member(member_id: int, member: MemberModel):
    session: Session = SessionLocal()
    try:
        existing_member = session.query(MemberSchema).filter(MemberSchema.id == member_id).first()

        if not existing_member:
            raise HTTPException(status_code=404, detail="ไม่พบข้อมูลสมาชิก")

        if member.code is not None:
            existing_member.code = member.code
        if member.name is not None:
            existing_member.name = member.name
        if member.phone is not None:
            existing_member.phone = member.phone
        if member.status is not None:
            existing_member.status = member.status

        updated_fields = {} 
        updated_fields = existing_member
        session.commit()

        return {
            "success": True,
            "message": "เเก้ไขข้อมูลสมาชิกสำเร็จ!",
            "id": member_id,
            "updated_data": updated_fields  
        }
    finally:
        session.close()

# ดึงข้อมูลตาม code จากตาราง tb_member
@router.get("/code/{member_code}")
def get_member_by_code(member_code: str):
    session = SessionLocal()
    try:
        member = session.query(MemberSchema).filter(MemberSchema.code == member_code).first()
        if not member:
            raise HTTPException(status_code=404, detail="ไม่พบข้อมูลสมาชิก")
        return {
            "message": "Get member by Code", 
            "row": {
                "code":member.code,
                "name":member.name,
                "phone": member.phone,
            }
        }
    finally:
        session.close()

# อัพเดทข้อมูลตาม code จากตาราง tb_member
@router.put("/code/{member_code}")
def update_member(member_code: str, member: MemberModel):
    session: Session = SessionLocal()
    try:
        existing_member = session.query(MemberSchema).filter(MemberSchema.code == member_code).first()

        if not existing_member:
            raise HTTPException(status_code=404, detail="ไม่พบข้อมูลสมาชิก")

        if member.phone is not None:
            existing_member.phone = member.phone


        updated_fields = {} 
        updated_fields = existing_member
        session.commit()

        return {
            "success": True,
            "message": "เเก้ไขข้อมูลสมาชิกสำเร็จ!",
            "code": member_code,
            "updated_data": updated_fields  
        }
    finally:
        session.close()