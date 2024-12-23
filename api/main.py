from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from database import SessionLocal, engine

# สร้างแอปพลิเคชัน FastAPI
app = FastAPI()

# ตั้งค่า CORS
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# กำหนด Base สำหรับการสร้าง Model
Base = declarative_base()

# สร้างตารางในฐานข้อมูล (หากยังไม่มี)
Base.metadata.create_all(bind=engine)

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

# ดึงข้อมูลจากตาราง tb_member
@app.get("/members")
def get_members():
    # สร้าง session
    session = SessionLocal()
    try:
        # ดึงข้อมูลทั้งหมดจากตาราง tb_member
        members = session.query(MemberGet).all() 
        # คืนค่าผลลัพธ์ในรูปแบบ JSON
        return {
            "message": "Get members",
            "rows": [{"id": member.id, "code": member.code, "name": member.name, "phone": member.phone, "status": member.status, "image": member.image} for member in members],
            "total": len(members)
        }
    finally:
        session.close()

# API สำหรับอัปเดทข้อมูลสมาชิก
@app.put("/members/{member_id}")
def update_member(member_id: int, member: MemberUpdate):
    # สร้าง session
    session = SessionLocal()
    try:
        # ค้นหาสมาชิกจาก id
        existing_member = session.query(MemberGet).filter(MemberGet.id == member_id).first() 

        # ถ้าหากไม่พบสมาชิก ให้ส่ง error
        if not existing_member:
            raise HTTPException(status_code=404, detail="Member not found")

        # อัปเดทข้อมูลสมาชิก
        existing_member.code = member.code
        existing_member.name = member.name
        existing_member.phone = member.phone
        existing_member.status = member.status
        existing_member.image = member.image

        # บันทึกการอัปเดท
        session.commit()

        # ส่งข้อมูลสมาชิกที่ถูกอัปเดทกลับ
        return {
            "message": "Update successful",
            # "id": existing_member.id,
            # "code": existing_member.code,
            # "name": existing_member.name,
            # "phone": existing_member.phone,
            # "status": existing_member.status,
            # "image": existing_member.image
        }
    finally:
        session.close()
