# router/product.py
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
import os
import base64
import uuid
from typing import List

from database import SessionLocal, engine
from model import ProductModel ,ProductImageModel
from schema import ProductSchema ,ProductImageSchema

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

def save_image_from_base64(base64_str: str, folder: str = "uploads") -> str:
    """
    ฟังก์ชันที่ใช้แปลง base64 string เป็นไฟล์รูปภาพ และบันทึกในโฟลเดอร์ที่กำหนด
    """
    try:
        # ตัด "data:image/png;base64," หรือ "data:image/jpeg;base64," ออก
        image_data = base64_str.split(",")[1]
        image_bytes = base64.b64decode(image_data)

        # กำหนดประเภทของไฟล์ตามชนิดใน Base64 (เช่น .jpeg, .png)
        file_extension = "png"  # กำหนดค่าเริ่มต้นเป็น png
        if base64_str.startswith("data:image/jpeg"):
            file_extension = "jpeg"
        elif base64_str.startswith("data:image/gif"):
            file_extension = "gif"
        
        # สร้างชื่อไฟล์ด้วย UUID
        filename = f"{uuid.uuid4()}.{file_extension}"
        file_path = os.path.join(folder, filename)

        # สร้างโฟลเดอร์ถ้ายังไม่มี
        os.makedirs(folder, exist_ok=True)

        # บันทึกไฟล์ลงในระบบ
        with open(file_path, "wb") as f:
            f.write(image_bytes)
        
        return file_path
    except Exception as e:
        raise HTTPException(status_code=400, detail="ไม่สามารถบันทึกรูปภาพได้")

@router.post("/product_image")
async def upload_images(product_images: list[str]):
    # สร้าง Session เองในที่นี้
    session = SessionLocal()
    image_filenames = []  # เก็บแค่ชื่อไฟล์
    try:
        for base64_image in product_images:
            # แปลง Base64 เป็นไฟล์
            file_path = save_image_from_base64(base64_image)
            # แยกแค่ชื่อไฟล์จาก path (เช่น "abc123.png")
            filename = os.path.basename(file_path)

            # บันทึกแค่ชื่อไฟล์ลงในฐานข้อมูล
            db_image = ProductImageSchema(path=filename)  # บันทึกแค่ชื่อไฟล์
            session.add(db_image)
            session.commit()
            session.refresh(db_image)

            # เก็บชื่อไฟล์ไว้เพื่อส่งกลับ
            image_filenames.append(db_image.path)

        return {"message": "บันทึกรูปภาพเรียบร้อย", "filenames": image_filenames}
    except Exception as e:
        # ในกรณีเกิดข้อผิดพลาดต้อง rollback การเปลี่ยนแปลงทั้งหมด
        session.rollback()
        raise HTTPException(status_code=500, detail="เกิดข้อผิดพลาดในการบันทึกข้อมูล")
    finally:
        # ปิดการเชื่อมต่อ session
        session.close()

@router.post("/add_data_product")
async def add_data_product(product: ProductModel, product_images: list[str] = []):
    session = SessionLocal()
    try:
        # 1. เพิ่มข้อมูลสินค้าใหม่
        new_product = ProductSchema(
            code=product.code,
            name=product.name,
            cost=product.cost,
            sell=product.sell,
            status=product.status,
            type=product.type,
            detail=product.detail
        )
        session.add(new_product)
        session.commit()  # commit เพื่อบันทึกสินค้าใหม่
        session.refresh(new_product)

        # 2. บันทึกข้อมูลภาพที่สัมพันธ์กับสินค้า
        image_filenames = []
        for base64_image in product_images:
            # แปลง Base64 เป็นไฟล์
            file_path = save_image_from_base64(base64_image)

            # แยกแค่ชื่อไฟล์จาก path
            filename = os.path.basename(file_path)

            # บันทึกภาพในฐานข้อมูล พร้อมกับ product_id ที่เชื่อมโยงกับสินค้าใหม่
            db_image = ProductImageSchema(
                path=filename,
                product_id=new_product.id  # เชื่อมโยงกับสินค้า
            )
            session.add(db_image)
            session.commit()
            session.refresh(db_image)

            image_filenames.append(db_image.path)

        return {"message": "เพิ่มสินค้าพร้อมรูปภาพสำเร็จ", "id": new_product.id, "filenames": image_filenames}
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail="เกิดข้อผิดพลาดในการบันทึกข้อมูล")
    finally:
        session.close()
