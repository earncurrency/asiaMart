# router/member.py
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc

from database import SessionLocal, engine
from model import MemberModel 
from schema import MemberSchema , Base

# สร้างตารางในฐานข้อมูล (หากยังไม่มี)
Base.metadata.create_all(bind=engine)

# สร้าง APIRouter สำหรับสมาชิก
router = APIRouter(
    prefix = "/members",
    tags = ["members"],
)

# ดึงข้อมูลจากตาราง tb_member
@router.get("/")
def get_members(limit: int = 10, offset: int = 0 ):
    session = SessionLocal()
    try:
        members = session.query(MemberSchema).order_by(desc(MemberSchema.id)).limit(limit).offset(offset).all()
        return {
            "message": "Get members",
            "rows": [{"id": member.id, "code": member.code, "name": member.name, "phone": member.phone, "status": member.status, "image": member.image} for member in members],
            "total": len(members)
        }
    finally:
        session.close()

# API สำหรับเพิ่มข้อมูลสมาชิก
@router.post("/")
def add_member(member: MemberModel):
    session = SessionLocal()
    try:
        # สร้างสมาชิกใหม่จากข้อมูลที่รับมา
        new_member = MemberSchema(
            code=member.code,
            name=member.name,
            phone=member.phone,
            status=member.status,
            image=member.image,
        )

        # เพิ่มสมาชิกใหม่ลงในฐานข้อมูล
        session.add(new_member)
        session.commit()

        # ส่งคืนข้อความการเพิ่มข้อมูลสำเร็จ
        return {"message": "Member added successfully", "id": new_member.id}
    finally:
        session.close()

@router.put("/{member_id}")
def update_member(member_id: int, member: MemberModel):
    session: Session = SessionLocal()
    try:
        existing_member = session.query(MemberSchema).filter(MemberSchema.id == member_id).first()

        if not existing_member:
            raise HTTPException(status_code=404, detail="Member not found")
        
        # อัปเดตเฉพาะฟิลด์ที่มีค่า
        if member.code is not None:
            existing_member.code = member.code
        if member.name is not None:
            existing_member.name = member.name
        if member.phone is not None:
            existing_member.phone = member.phone
        if member.status is not None:
            existing_member.status = member.status
        if member.image is not None:
            existing_member.image = member.image

        session.commit()

        return {
            "success": True,
            "message": "Update successful",
            "id": member_id
        }
    finally:
        session.close()
