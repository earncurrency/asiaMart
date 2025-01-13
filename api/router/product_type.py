# router/product_type.py
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc

from database import SessionLocal, engine
from model import ProductTypeModel 
from schema import ProductTypeSchema 

# สร้าง APIRouter สำหรับสมาชิก
router = APIRouter(
    prefix = "/product_type",
    tags = ["product_type"],
)

# ดึงข้อมูลทั้งหมดจากตาราง tb_product_type
@router.get("/")
def product_types(limit: int = 10, offset: int = 0):
    session = SessionLocal()
    try:
        types = session.query(ProductTypeSchema).order_by(desc(ProductTypeSchema.id)).limit(limit).offset(offset).all()
        total_types = session.query(ProductTypeSchema).count()
        return {
            "message": "Get all product types",
            "rows": [{"id": type.id, "name": type.name, "status": type.status} for type in types],
            "total": total_types
        }
    finally:
        session.close()

# ดึงข้อมูลตามไอดีจากตาราง tb_product_type
@router.get("/{product_type_id}")
def product_type(product_type_id: int):
    session = SessionLocal()
    try:
        product_type = session.query(ProductTypeSchema).filter(ProductTypeSchema.id == product_type_id).first()
        if not product_type:
            raise HTTPException(status_code=404, detail="ไม่พบข้อมูลประเภทสินค้า")
        return {
            "message": "Get product type by ID",
            "row": {"id": product_type.id, "name": product_type.name, "status": product_type.status}
        }
    finally:
        session.close()