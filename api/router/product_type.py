# router/product_type.py
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc

from database import SessionLocal, engine
from model import ProductTypeModel 
from schema import ProductTypeSchema 

# สร้าง APIRouter สำหรับประเภทสินค้า
router = APIRouter(
    prefix = "/product_type",
    tags = ["product_type"],
)

# ดึงข้อมูลทั้งหมดจากตาราง tb_product_type ยกเว้นที่ remove
@router.get("/get_product_type_not_remove")
def product_types(limit: int = 10, offset: int = 0):
    session = SessionLocal()
    try:
        types = session.query(ProductTypeSchema).filter(ProductTypeSchema.status != 'remove').order_by(desc(ProductTypeSchema.id)).limit(limit).offset(offset).all()
        total_types = session.query(ProductTypeSchema).count()
        return {
            "message": "Get all product types",
            "rows": [{"id": type.id, "name": type.name, "status": type.status} for type in types],
            "total": total_types
        }
    finally:
        session.close()

@router.get("/get_product_type_active")
def product_types(limit: int = 10, offset: int = 0):
    session = SessionLocal()
    try:
        types = session.query(ProductTypeSchema).filter(ProductTypeSchema.status == 'active').order_by(desc(ProductTypeSchema.id)).limit(limit).offset(offset).all()
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

# API สำหรับเพิ่มข้อมูลประเภทสินค้า
@router.post("/add_product_type")
async def add_product_type(product_type: ProductTypeModel):
    session = SessionLocal()
    try:
        # 1. เพิ่มข้อมูลสินค้าใหม่
        new_product_type = ProductTypeSchema(
            name=product_type.name,
            status=product_type.status,
        )
        session.add(new_product_type)
        session.commit()  
        session.refresh(new_product_type)

        return {
            "success": True,
            "message": "บันทึกข้อมูลสินค้าสำเร็จ",
            "updated_data": new_product_type
        }
    finally:
        session.close()

# API สำหรับอัปเดทข้อมูลประเภทสินค้า
@router.put("/update_product_type/{product_type_id}")
def update_product_type(product_type_id: int, product_type: ProductTypeModel):
    session: Session = SessionLocal()
    try:
        existing_product_type = session.query(ProductTypeSchema).filter(ProductTypeSchema.id == product_type_id).first()

        if not existing_product_type:
            raise HTTPException(status_code=404, detail="ไม่พบข้อมูลประเภทสินค้า")

        if product_type.name is not None:
            existing_product_type.name = product_type.name
        if product_type.status is not None:
            existing_product_type.status = product_type.status

        updated_fields = {} 
        updated_fields = existing_product_type
        session.commit()

        return {
            "success": True,
            "message": "เเก้ไขข้อมูลสมาชิกสำเร็จ!",
            "id": product_type_id,
            "updated_data": updated_fields  
        }
    finally:
        session.close()

@router.put("/remove_product_type/{product_type_id}")
def remove_product_type(product_type_id: int):
    session: Session = SessionLocal()  # สร้าง session ใหม่

    try:
        # ค้นหาสินค้าจาก product_id
        existing_product_type = session.query(ProductTypeSchema).filter(ProductTypeSchema.id == product_type_id).first()

        # เปลี่ยนสถานะสินค้าเป็น remove
        existing_product_type.status = "remove"

        # บันทึกการเปลี่ยนแปลง
        session.commit()

        # อัปเดตข้อมูลสินค้าและส่งกลับ
        session.refresh(existing_product_type)

        return {
            "success": True,
            "message": "อัปเดตสถานะประเภทสินค้าเป็น remove สำเร็จ",
            "updated_data": existing_product_type
        }

    finally:
        session.close()  # ปิด session