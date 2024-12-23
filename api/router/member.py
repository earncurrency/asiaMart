# router/member.py
from fastapi import APIRouter, HTTPException
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, engine
from sqlalchemy.ext.declarative import declarative_base

# สร้าง Base สำหรับการสร้าง Model
Base = declarative_base()

# สร้าง โครงสร้างของตาราง tb_member
class SchemaMember(Base):
    
    __tablename__ = "tb_member"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(10))
    name = Column(String(50))
    phone = Column(String(15))
    status = Column(String(15))
    image = Column(String(255))

# สร้างตารางในฐานข้อมูล (หากยังไม่มี)
Base.metadata.create_all(bind=engine)

# Pydantic model โครงสร้างข้อมูล สำหรับการรับข้อมูลที่ต้องการอัปเดท
class ModelMember(BaseModel):
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
)

# ดึงข้อมูลจากตาราง tb_member
@router.get("/")
def get_members():
    session = SessionLocal()
    try:
        members = session.query(SchemaMember).all()
        return {
            "message": "Get members",
            "rows": [{"id": member.id, "code": member.code, "name": member.name, "phone": member.phone, "status": member.status, "image": member.image} for member in members],
            "total": len(members)
        }
    finally:
        session.close()

# API สำหรับเพิ่มข้อมูลสมาชิก
@router.post("/")
def add_member(member: ModelMember):
    session = SessionLocal()
    try:
        # สร้างสมาชิกใหม่จากข้อมูลที่รับมา
        new_member = SchemaMember(
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


# API สำหรับอัปเดทข้อมูลสมาชิก
@router.put("/{member_id}")
def update_member(member_id: int, member: ModelMember):
    session = SessionLocal()
    try:
        existing_member = session.query(SchemaMember).filter(SchemaMember.id == member_id).first()

        if not existing_member:
            raise HTTPException(status_code=404, detail="Member not found")
        
        existing_member.code = member.code
        existing_member.name = member.name
        existing_member.phone = member.phone
        existing_member.status = member.status
        existing_member.image = member.image

        session.commit()

        return {"message": "Update successful" ,"id": member_id}
    finally:
        session.close()
