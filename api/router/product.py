# router/product.py
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal, engine
from model import ProductModel 
from schema import ProductSchema , Base
# สร้างตารางในฐานข้อมูล (หากยังไม่มี)
Base.metadata.create_all(bind=engine)

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
        products = session.query(ProductSchema).all()
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
def update_product(product_id: int, product: ProductModel):
    session = SessionLocal()
    try:
        existing_product = session.query(ProductSchema).filter(ProductSchema.id == product_id).first()

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