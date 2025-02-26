# router/product.py
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session ,aliased
from sqlalchemy import asc, desc

import os ,base64 ,uuid, math
from typing import List

from database import SessionLocal, engine
from model import ProductModel ,ProductImageModel
from schema import ProductSchema ,ProductImageSchema, CategorySchema

# สร้าง APIRouter สำหรับสมาชิก
router = APIRouter(
    prefix = "/products",
    tags = ["products"],
)

# ดึงข้อมูลทั้งหมดจากตาราง tb_product
@router.get("/")
def get_products_by_category_id(page: int = 1, limit: int = 5, category_id: str = '', status: str = '', q: str = '',):
    session = SessionLocal()

    offset = (page * limit) - limit

    try:
        print(f"category_id = {category_id} limit = {limit} page = {page} q = {q} offset = {offset}")

        query = session.query(ProductSchema).filter(ProductSchema.status != 'remove')

        if category_id:
            query = query.filter(ProductSchema.category_id == category_id)

        if status:
            query = query.filter(ProductSchema.status == status)

        if q:
            query = query.filter(ProductSchema.name.ilike(f'%{q}%') ,ProductSchema.status == 'active')

        products = query.order_by(desc(ProductSchema.id)).limit(limit).offset(offset).all()

        total = query.count()

        # สร้างผลลัพธ์ที่ต้องการส่งกลับ
        result = []
        for product in products:
            product_images = session.query(ProductImageSchema).filter(
                ProductImageSchema.product_id == product.id,
                ProductImageSchema.status == 'active'
            ).all()
            image_paths = [image.path for image in product_images]

            result.append({
                "id": product.id,
                "code": product.code,
                "name": product.name,
                "cost": product.cost,
                "price": product.price,
                "status": product.status,
                "category_id": product.category_id,
                "detail": product.detail,
                "images": image_paths
            })

        return {
            "message": "Get active products by category",
            "rows": result,
            "total": total
        }

    finally:
        session.close()

#ดึงข้อมูลสินค้าตามไอดีจากตาราง tb_product
@router.get("/{product_id}")
def get_product(product_id: int):
    session = SessionLocal()
    try:
        # ทำการ query และ join ข้อมูลจาก tb_product และ tb_product_image โดยกรองตาม product_id และ filter status ของสินค้า
        product = session.query(ProductSchema).join(
            ProductImageSchema, ProductImageSchema.product_id == ProductSchema.id, isouter=True
        ).filter(ProductSchema.id == product_id).first()

        # ดึงข้อมูลรูปภาพทั้งหมดที่เกี่ยวข้องกับ product_id และ filter status เป็น 'active'
        product_images = session.query(ProductImageSchema).filter(
            ProductImageSchema.product_id == product.id,ProductImageSchema.status == 'active').all()

        # สร้างรายการรูปภาพที่เกี่ยวข้อง
        image_data = [{"id": image.id, "path": image.path} for image in product_images]

        return {
            "message": "Get product by product_id",
            "row": {
                "id": product.id,
                "code": product.code,
                "name": product.name,
                "cost": product.cost,
                "price": product.price,
                "status": product.status,
                "category_id": product.category_id,
                "detail": product.detail,
                "images": image_data  # ส่งข้อมูลภาพทั้งหมดที่เกี่ยวข้องกับสินค้า
            }
        }

    finally:
        session.close()

# API สำหรับเพิ่มข้อมูลสินค้า เเละรูปภาพ
@router.post("/")
async def add_product(product: ProductModel,product_images: list[str] = []):
    session = SessionLocal()
    try:
        # 1. เพิ่มข้อมูลสินค้าใหม่
        new_product = ProductSchema(
            code=product.code,
            name=product.name,
            cost=product.cost,
            price=product.price,
            status=product.status,
            category_id=product.category_id,
            detail=product.detail,
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
                product_id=new_product.id ,
                status="active"
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
        if product.price is not None:
            existing_member.price = product.price
        if product.status is not None:
            existing_member.status = product.status
        if product.category_id is not None: 
            existing_member.category_id = product.category_id
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
                product_id=product_id,
                status="active"
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

@router.delete("/{product_id}")
def remove_product(product_id: int):
    session: Session = SessionLocal()  # สร้าง session ใหม่

    try:
        # ค้นหาสินค้าจาก product_id
        existing_product = session.query(ProductSchema).filter(ProductSchema.id == product_id).first()

        # เปลี่ยนสถานะสินค้าเป็น remove
        existing_product.status = "remove"

        # บันทึกการเปลี่ยนแปลง
        session.commit()

        # อัปเดตข้อมูลสินค้าและส่งกลับ
        session.refresh(existing_product)

        return {
            "success": True,
            "message": "อัปเดตสถานะสินค้าเป็น remove สำเร็จ",
            "updated_data": existing_product
        }

    finally:
        session.close()  # ปิด session

@router.delete("/image/{image_id}")
def remove_image_product(image_id: int):
    session: Session = SessionLocal()  # สร้าง session ใหม่

    try:
        # ค้นหาสินค้าจาก image_id
        existing_image = session.query(ProductImageSchema).filter(ProductImageSchema.id == image_id).first()

        # เปลี่ยนสถานะสินค้าเป็น remove
        existing_image.status = "remove"

        # บันทึกการเปลี่ยนแปลง
        session.commit()

        # อัปเดตข้อมูลสินค้าและส่งกลับ
        session.refresh(existing_image)

        return {
            "success": True,
            "message": "อัปเดตสถานะรูปภาพสินค้าเป็น remove สำเร็จ",
            "updated_data": existing_image
        }

    finally:
        session.close()  # ปิด session

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

@router.get("/cat/")
def get_products_by_category_id(category_id: str = '', limit: int = 10, q: str = '', page: int = 1):  
    session = SessionLocal()

    offset = (page * limit) - limit; 

    try:
        print(f"category_id = {category_id} limit = {limit} page = {page} q = {q}")

        query = session.query(ProductSchema).filter(ProductSchema.status == 'active')

        if category_id:
            query = query.filter(ProductSchema.category_id == category_id)

        if q:
            query = query.filter(ProductSchema.name.ilike(f'%{q}%'))

        products = query.order_by(desc(ProductSchema.id)).limit(limit).offset(offset).all()

        total = query.count()

        # สร้างผลลัพธ์ที่ต้องการส่งกลับ
        result = []
        for product in products:
            product_images = session.query(ProductImageSchema).filter(
                ProductImageSchema.product_id == product.id,
                ProductImageSchema.status == 'active'
            ).all()
            image_paths = [image.path for image in product_images]

            result.append({
                "id": product.id,
                "code": product.code,
                "name": product.name,
                "cost": product.cost,
                "price": product.price,
                "status": product.status,
                "category_id": product.category_id,
                "detail": product.detail,
                "images": image_paths
            })

        return {
            "message": "Get active products by category",
            "rows": result,
            "total": total
        }

    finally:
        session.close()

@router.get("/search/")
def get_products_by_q(q: str = ''):
    session = SessionLocal()

    try:
        print(f"q = {q}")

        if not q:
            return {
                "message": "ไม่มีข้อมูลที่ค้นหา.",
                "rows": [],
                "total": 0
            }

        # สร้าง query พื้นฐาน
        query = session.query(ProductSchema).filter(
            ProductSchema.name.ilike(f'%{q}%'),
            ProductSchema.status == 'active'
        )

        # ดึงข้อมูลและเรียงลำดับตาม id จากมากไปน้อย
        products = query.order_by(desc(ProductSchema.id)).all()
        total = query.count()

        # สร้างผลลัพธ์ที่ต้องการส่งกลับ
        result = []
        for product in products:
            # ดึงรูปภาพสินค้า
            product_images = session.query(ProductImageSchema).filter(
                ProductImageSchema.product_id == product.id,
                ProductImageSchema.status == 'active'
            ).all()
            image_paths = [image.path for image in product_images]

            # เพิ่มข้อมูลสินค้าในผลลัพธ์
            result.append({
                "id": product.id,
                "code": product.code,
                "name": product.name,
                "cost": product.cost,
                "price": product.price,
                "status": product.status,
                "category_id": product.category_id,
                "detail": product.detail,
                "images": image_paths
            })

        return {
            "message": f"พบ {total} สินค้าที่ '{q}'",
            "rows": result,
            "total": total
        }

    finally:
        session.close()