from sqlalchemy import Column, Integer, String, Float, TIMESTAMP ,Date
from sqlalchemy.ext.declarative import declarative_base
from database import engine

Base = declarative_base()

# สร้าง โครงสร้างของตาราง tb_member
class MemberSchema(Base):

    __tablename__ = "tb_member"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(15))
    name = Column(String(50))
    phone = Column(String(15))
    status = Column(String(15))

#สร้าง โครงสร้างของตาราง tb_product
class ProductSchema(Base):

    __tablename__ = "tb_product"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(15))
    name = Column(String(50))
    cost = Column(Float)
    price = Column(Float)
    status = Column(String(15))
    category_id = Column(Integer)
    detail = Column(String(255))

#สร้าง โครงสร้างของตาราง tb_product_image
class ProductImageSchema(Base):

    __tablename__ = "tb_product_image"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer)
    path = Column(String(255))  
    status = Column(String(15))

#สร้าง โครงสร้างของตาราง tb_category
class CategorySchema(Base):

    __tablename__ = "tb_category"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(15))
    status = Column(String(15))  


class OrderSchema(Base):

    __tablename__ = "tb_order"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20))
    order_date = Column(TIMESTAMP)
    member_id = Column(Integer)
    member_name = Column(String(30))
    member_phone = Column(String(15))
    address = Column(String(25))
    total = Column(Float)
    status = Column(String(15))
    length = Column(Integer)


class OrderDetailSchema(Base):

    __tablename__ = "tb_order_detail"    
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer)
    product_id = Column(Integer)
    product_name = Column(String(50))
    product_price = Column(Float)
    qty = Column(Integer)


class AdminSchema(Base):

    __tablename__ = "tb_admin"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(15))
    name = Column(String(50))
    phone = Column(String(15))
    status = Column(String(15))


class RecommendSchema(Base):

    __tablename__ = "tb_recommend"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer)
    start_date = Column(Date)
    end_date = Column(Date)
    
# สร้างตารางในฐานข้อมูล (หากยังไม่มี)
Base.metadata.create_all(bind=engine)
