from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal, engine

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.future import select

app = FastAPI()

origins = [
    "*",
]

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
class Member(Base):
    __tablename__ = "tb_member"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    phone = Column(String(15))
    status = Column(String(15))
    image = Column(String(255))


# ฟังก์ชั่นในการดึงข้อมูลจากตาราง tb_member
@app.get("/members")
def get_members():
    # สร้าง session
    session = SessionLocal()
    try:
        # ดึงข้อมูลทั้งหมดจากตาราง tb_member
        members = session.query(Member).all()
        # คืนค่าผลลัพธ์ในรูปแบบ JSON
        return {
            "rows": [{"id": member.id, "name": member.name, "phone": member.phone, "status": member.status, "image": member.image} for member in members],
            "total":10
        }
    finally:
        session.close()
