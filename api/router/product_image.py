from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import SessionLocal, engine
from model import ProductImageModel
from schema import ProductImageSchema 

# สร้าง APIRouter สำหรับสมาชิก
router = APIRouter(
    prefix="/product_image",
    tags=["product_image"],
)

# เพิ่มรูปภาพสินค้า (หลายรูปภาพ)
@router.post("/")
def add_product_image(p_images: List[ProductImageModel]):
    session = SessionLocal()
    try:
        # สร้างรายการของรูปภาพที่ต้องการเพิ่ม
        new_product_images = []
        for p_image in p_images:
            new_product_image = ProductImageSchema(
                product_id=p_image.product_id,
                path=p_image.path,
            )
            new_product_images.append(new_product_image)
        
        # เพิ่มข้อมูลหลายๆ รูปภาพลงในฐานข้อมูล
        session.add_all(new_product_images)
        session.commit()

        # ส่งคืนข้อความการเพิ่มข้อมูลสำเร็จ
        return {"message": "เพิ่มรูปภาพสินค้าสำเร็จ", "ids": [img.id for img in new_product_images]}
    finally:
        session.close()
