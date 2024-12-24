# router/product.py
from fastapi import APIRouter, HTTPException
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, engine
from sqlalchemy.ext.declarative import declarative_base

# สร้าง base สำหรับการสร้าง Modal
Base = declarative_base()

#สร้าง โครงสร้างของตาราง tb_product
class SchemaProduct(Base):

    __tablename__ = "tb_product"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(10))
    name = Column(String(50))
    cost = Column(String(10))
    sell = Column(String(10))
    status = Column(String(15))
    
# สร้างตารางในฐานข้อมูล (หากยังไม่มี)
Base.metadata.create_all(bind=engine)

# Pydantic model โครงสร้างข้อมูล สำหรับการรับข้อมูลที่ต้องการอัปเดท
class ModelProduct(BaseModel):  
    code: str
    name: str
    cost: str
    sell: str
    status: str

    class Config:
        orm_mode = True
        
# สร้าง APIRouter สำหรับสมาชิก
router = APIRouter(
    prefix = "/products",
    tags = ["products"],
)

# ดึงข้อมูลจากตาราง tb_product
@router.get("/")
def get_products():
    session = SessionLocal()
    try:
        products = session.query(SchemaProduct).all()
        return {
            "message": "Get products",
            "rows": [{"id": product.id, "code": product.code, "name": product.name, 
                      "cost": product.cost, "sell": product.sell, "status": product.status} for product in products],
            "total": len(products)
        }
    finally:
        session.close()    
        
# API สำหรับเพิ่มข้อมูลสินค้า
@router.post("/")
def add_product(product: ModelProduct):
    session = SessionLocal()
    try:
        # สร้างสมาชิกใหม่จากข้อมูลที่รับมา
        new_product = SchemaProduct(
            code=product.code,
            name=product.name,
            cost=product.cost,
            sell=product.sell,
            status=product.status,
        )

        # เพิ่มสินค้าใหม่ลงในฐานข้อมูล
        session.add(new_product)
        session.commit()

        # ส่งคืนข้อความการเพิ่มข้อมูลสำเร็จ
        return {"message": "Product added successfully", "id": new_product.id}
    finally:
        session.close()
        
# API สำหรับอัปเดทข้อมูลสินค้า
@router.put("/{product_id}")
def update_product(product_id: int, product: ModelProduct):
    session = SessionLocal()
    try:
        existing_product = session.query(SchemaProduct).filter(SchemaProduct.id == product_id).first()

        if not existing_product:
            raise HTTPException(status_code=404, detail="Product not found")
        
        existing_product.code = product.code
        existing_product.name = product.name
        existing_product.cost = product.cost
        existing_product.sell = product.sell
        existing_product.status = product.status

        session.commit()

        return {"message": "Update successful" ,"id": product_id}
    finally:
        session.close()        