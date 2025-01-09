# router/product.py
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session ,aliased
from sqlalchemy import asc, desc
import os ,base64 ,uuid, math
from typing import List

from database import SessionLocal, engine
from model import ProductModel ,ProductImageModel
from schema import ProductSchema ,ProductImageSchema

# สร้าง APIRouter สำหรับสมาชิก
router = APIRouter(
    prefix = "/products",
    tags = ["products"],
)

# ดึงข้อมูลทั้งหมดจากตาราง tb_product
@router.get("/")
def get_products():
    session = SessionLocal()
    try:
        # ทำการ query และ join ข้อมูลจาก tb_product และ tb_product_image
        products = session.query(ProductSchema).join(
            ProductImageSchema, ProductImageSchema.product_id == ProductSchema.id, isouter=True
        ).order_by(desc(ProductSchema.id)).all()

        # สร้างผลลัพธ์ที่จะส่งกลับ
        result = []
        for product in products:
            # ดึงข้อมูลภาพ (ถ้ามี)
            product_images = session.query(ProductImageSchema).filter(ProductImageSchema.product_id == product.id).all()

            # สร้างรายการรูปภาพที่เกี่ยวข้อง
            image_paths = [image.path for image in product_images]

            result.append({
                "id": product.id,
                "code": product.code,
                "name": product.name,
                "cost": product.cost,
                "sell": product.sell,
                "status": product.status,
                "type": product.type,
                "detail": product.detail,
                "images": image_paths  # ส่งข้อมูลภาพทั้งหมดที่เกี่ยวข้องกับสินค้า
            })

        return {
            "message": "Get products",
            "rows": result,
            "total": len(result)
        }

    finally:
        session.close() 
    
#ดึงข้อมูลสินค้าตามไอดีจากตาราง tb_product
@router.get("/{product_id}")
def get_product_by_id(product_id: int):
    session = SessionLocal()
    try:
        # ทำการ query และ join ข้อมูลจาก tb_product และ tb_product_image โดยกรองตาม product_id
        product = session.query(ProductSchema).join(
            ProductImageSchema, ProductImageSchema.product_id == ProductSchema.id, isouter=True
        ).filter(ProductSchema.id == product_id).first()

        if not product:
            raise HTTPException(status_code=404, detail="ไม่พบข้อมูลสินค้าตาม ID ที่ระบุ")

        # ดึงข้อมูลรูปภาพทั้งหมดที่เกี่ยวข้องกับ product_id
        product_images = session.query(ProductImageSchema).filter(ProductImageSchema.product_id == product.id).all()

        # สร้างรายการรูปภาพที่เกี่ยวข้อง
        image_paths = [image.path for image in product_images]

        return {
            "message": "Get product by product_id",
            "row": {
                "id": product.id,
                "code": product.code,
                "name": product.name,
                "cost": product.cost,
                "sell": product.sell,
                "status": product.status,
                "type": product.type,
                "detail": product.detail,
                "images": image_paths  # ส่งข้อมูลภาพทั้งหมดที่เกี่ยวข้องกับสินค้า
            }
        }

    finally:
        session.close()  

#ฟังก์ชันที่ใช้แปลง base64 string เป็นไฟล์รูปภาพ
def save_image_from_base64(base64_str: str, folder: str ) -> str:
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

# API สำหรับเพิ่มข้อมูลสินค้า เเละรูปภาพ
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

        uploadPath = 'uploads/' + str(math.ceil(new_product.id / 100))

        image_filenames = []
        for base64_image in product_images:
            # แปลง Base64 เป็นไฟล์
            file_path = save_image_from_base64(base64_image,uploadPath)

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

        return {
            "success": True,
            "message": "บันทึกข้อมูลสินค้าสำเร็จ",
            "updated_data": new_product  
        }
    finally:
        session.close()

# API สำหรับอัปเดทข้อมูลสินค้า
@router.put("/{product_id}")
def update_product(product_id: int, product: ProductModel, product_images: list[str] = []):
    session: Session = SessionLocal()
    try:
        existing_member = session.query(ProductSchema).filter(ProductSchema.id == product_id).first()

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

        # 2. บันทึกข้อมูลภาพที่สัมพันธ์กับสินค้า

        uploadPath = 'uploads/' + str(math.ceil(product_id / 100))

        image_filenames = []
        for base64_image in product_images:
            # แปลง Base64 เป็นไฟล์
            file_path = save_image_from_base64(base64_image,uploadPath)

            # แยกแค่ชื่อไฟล์จาก path
            filename = os.path.basename(file_path)

            # บันทึกภาพในฐานข้อมูล พร้อมกับ product_id ที่เชื่อมโยงกับสินค้าใหม่
            db_image = ProductImageSchema(
                path=filename,
                product_id=product_id  # เชื่อมโยงกับสินค้า
            )
            session.add(db_image)
            session.commit()
            session.refresh(db_image)

            image_filenames.append(db_image.path)

        return {
            "success": True,
            "message": "เเก้ไขข้อมูลสินค้าสำเร็จ",
            "updated_data": product
        }
    finally:
        session.close()
