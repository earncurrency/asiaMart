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

# ดึงข้อมูลทั้งหมดจากตาราง tb_member
@router.get("/")
def get_members(limit: int = 10, offset: int = 0):
    session = SessionLocal()
    try:
        members = session.query(MemberSchema).order_by(desc(MemberSchema.id)).limit(limit).offset(offset).all()
        total_members = session.query(MemberSchema).count()
        return {
            "message": "Get all members",
            "rows": [{"id": member.id, "code": member.code, "name": member.name, "phone": member.phone, "status": member.status} for member in members],
            "total": total_members
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
            raise HTTPException(status_code=404, detail="Member not found")
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
        # สร้างสมาชิกใหม่จากข้อมูลที่รับมา
        new_member = MemberSchema(
            code=member.code,
            name=member.name,
            phone=member.phone,
            status=member.status,
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
            "message": "Update successful",
            "id": member_id,
            "updated_data": updated_fields  
        }
    finally:
        session.close()

