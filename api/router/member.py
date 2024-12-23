# router/member.py
from fastapi import APIRouter, HTTPException
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, engine
from sqlalchemy.ext.declarative import declarative_base

# สร้าง Base สำหรับการสร้าง Model
Base = declarative_base()

# สร้าง Model สำหรับตาราง tb_member
class MemberGet(Base):
    __tablename__ = "tb_member"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(10))
    name = Column(String(50))
    phone = Column(String(15))
    status = Column(String(15))
    image = Column(String(255))

# Pydantic model สำหรับการรับข้อมูลที่ต้องการอัปเดท
class MemberUpdate(BaseModel):
    code: str
    name: str
    phone: str
    status: str
    image: str

    class Config:
        orm_mode = True

# สร้าง APIRouter สำหรับสมาชิก
router = APIRouter(
    prefix = "/members",
    tags = ["members"],
    # responses = {
    #     404: { "description": "Not found" }
    # },
)

# ดึงข้อมูลจากตาราง tb_member
@router.get("/members")
def get_members():
    session = SessionLocal()
    try:
        members = session.query(MemberGet).all()
        return {
            "message": "Get members",
            "rows": [{"id": member.id, "code": member.code, "name": member.name, "phone": member.phone, "status": member.status, "image": member.image} for member in members],
            "total": len(members)
        }
    finally:
        session.close()

# API สำหรับอัปเดทข้อมูลสมาชิก
@router.put("/members/{member_id}")
def update_member(member_id: int, member: MemberUpdate):
    session = SessionLocal()
    try:
        existing_member = session.query(MemberGet).filter(MemberGet.id == member_id).first()

        if not existing_member:
            raise HTTPException(status_code=404, detail="Member not found")

        existing_member.code = member.code
        existing_member.name = member.name
        existing_member.phone = member.phone
        existing_member.status = member.status
        existing_member.image = member.image

        session.commit()

        return {"message": "Update successful"}
    finally:
        session.close()

# สร้างตารางในฐานข้อมูล (หากยังไม่มี)
Base.metadata.create_all(bind=engine)
