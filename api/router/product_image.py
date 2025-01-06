import os
import base64
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
import uuid

from database import SessionLocal
from model import ProductImageModel
from schema import ProductImageSchema 

# สร้าง APIRouter สำหรับสมาชิก
router = APIRouter(
    prefix="/product_image",
    tags=["product_image"],
)

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

@router.post("/")
async def upload_images(product_images: list[str]):

    # สร้าง Session เองในที่นี้
    session = SessionLocal()
    image_paths = []
    try:
        for base64_image in product_images:
            # แปลง Base64 เป็นไฟล์
            file_path = save_image_from_base64(base64_image)

            # บันทึกข้อมูล path ของไฟล์ลงในฐานข้อมูล
            db_image = ProductImageSchema(path=file_path)
            session.add(db_image)
            session.commit()
            session.refresh(db_image)

            # เก็บ path ไฟล์ไว้เพื่อส่งกลับ
            image_paths.append(db_image.path)
        
        return {"message": "บันทึกรูปภาพเรียบร้อย", "paths": image_paths}
    except Exception as e:
        # ในกรณีเกิดข้อผิดพลาดต้อง rollback การเปลี่ยนแปลงทั้งหมด
        session.rollback()
        raise HTTPException(status_code=500, detail="เกิดข้อผิดพลาดในการบันทึกข้อมูล")
    finally:
        # ปิดการเชื่อมต่อ session
        session.close()
