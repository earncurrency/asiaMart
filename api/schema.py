from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from database import engine

Base = declarative_base()

# สร้างตารางในฐานข้อมูล (หากยังไม่มี)
Base.metadata.create_all(bind=engine)

# สร้าง โครงสร้างของตาราง tb_member
class MemberSchema(Base):
    
    __tablename__ = "tb_member"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(10))
    name = Column(String(50))
    phone = Column(String(15))
    status = Column(String(15))

#สร้าง โครงสร้างของตาราง tb_product
class ProductSchema(Base):

    __tablename__ = "tb_product"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(10))
    name = Column(String(50))
    cost = Column(String(10))
    sell = Column(String(10))
    status = Column(String(15))
    type = Column(String(15))
    detail = Column(String(255))
    
