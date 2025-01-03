# router/product.py
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc

from database import SessionLocal, engine
from model import ProductModel 
from schema import ProductSchema

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
        products = session.query(ProductSchema).order_by(desc(ProductSchema.id)).all()
        return {
            "message": "Get products",
            "rows": [{"id": product.id, "code": product.code, "name": product.name, 
                      "cost": product.cost, "sell": product.sell, "status": product.status , "type": product.type , "detail":product.detail} for product in products],
            "total": len(products)
        }
    finally:
        session.close()    
        
#ดึงข้อมูลตามไอดีจากตาราง tb_product
@router.get("/{product_id}")
def get_product(product_id:int):
    session = SessionLocal()
    try:
        product = session.query(ProductSchema).filter(ProductSchema.id == product_id).first()
        if not product:
            raise HTTPException(status_code=404, detail="ไม่พบข้อมูลสินค้า")
        return {
            "message": "Get product by ID",
            "row": {"id": product.id, "code": product.code, "name": product.name, "cost": product.cost, "sell": product.sell, "status": product.status , "type": product.type , "detail":product.detail}
        }    
    finally:
        session.close()    

# API สำหรับเพิ่มข้อมูลสินค้า
@router.post("/")
def add_product(product: ProductModel):
    session = SessionLocal()
    try:
        # สร้างสมาชิกใหม่จากข้อมูลที่รับมา
        new_product = ProductSchema(
            code=product.code,
            name=product.name,
            cost=product.cost,
            sell=product.sell,
            status=product.status,
            type=product.type,
            detail=product.detail
        )

        # เพิ่มสินค้าใหม่ลงในฐานข้อมูล
        session.add(new_product)
        session.commit()

        # ส่งคืนข้อความการเพิ่มข้อมูลสำเร็จ
        return {"message": "เพิ่มสินค้าสำเร็จ", "id": new_product.id}
    finally:
        session.close()
        
# API สำหรับอัปเดทข้อมูลสินค้า
@router.put("/{product_id}")
def update_product(product_id: int, product: ProductModel):
    session: Session = SessionLocal()
    try:
        existing_member = session.query(ProductSchema).filter(ProductSchema.id == product_id).first()

        if not existing_member:
            raise HTTPException(status_code=404, detail="ไม่พบข้อมูลสินค้า")

        if product.code is not None:
            existing_member.code = product.code
        if product.name is not None:
            existing_member.name = product.name
        if product.cost is not None:
            existing_member.cost = product.cost
        if product.sell is not None:
            existing_member.sell = product.sell
        if product.status is not None:
            existing_member.status = product.status
        if product.type is not None: 
            existing_member.type = product.type
        if product.detail is not None: 
            existing_member.detail = product.detail    

        updated_fields = {} 
        updated_fields = existing_member
        session.commit()

        return {
            "success": True,
            "message": "เเก้ไขข้อมูลสินค้าสำเร็จ",
            "id": product_id,
            "updated_data": updated_fields  
        }
    finally:
        session.close()