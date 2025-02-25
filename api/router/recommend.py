# router/product.py
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session ,aliased
from sqlalchemy import asc, desc
import os ,base64 ,uuid, math
from typing import List

from database import SessionLocal, engine
from model import ProductModel ,ProductImageModel , RecommendModel
from schema import ProductSchema ,ProductImageSchema, CategorySchema ,  RecommendSchema

# สร้าง APIRouter สำหรับสมาชิก
router = APIRouter(
    prefix = "/recommends",
    tags = ["recommends"],
)
@router.get("/")
def get_recommends(limit: int = 10, q: str = '', page: int = 1 , status: str = ''):
    session = SessionLocal()
    
    offset = (page * limit) - limit
    
    try:

        query = session.query(RecommendSchema).join(
            ProductSchema,
            RecommendSchema.product_id == ProductSchema.id
        ).filter(ProductSchema.status != 'remove')

        query = query.filter(RecommendSchema.status != 'remove')

        if q:
            query = query.filter(ProductSchema.name.ilike(f'%{q}%'))

        if status:
            query = query.filter(RecommendSchema.status == status)    

        recommends = query.order_by(desc(RecommendSchema.id)).limit(limit).offset(offset).all()
        
        total = query.count()

        result = []
        for recommend in recommends:
            # Get product
            product = session.query(ProductSchema).filter(
                ProductSchema.id == recommend.product_id
            ).first()

            # Get product images
            product_images = session.query(ProductImageSchema).filter(
                ProductImageSchema.product_id == product.id,
                ProductImageSchema.status == 'active'
            ).all()
            image_paths = [image.path for image in product_images]

            result.append({
                "id": recommend.id,
                "code": product.code,
                "name": product.name,
                "images": image_paths,
                "start_date": recommend.start_date.strftime("%Y-%m-%d"),
                "end_date": recommend.end_date.strftime("%Y-%m-%d"),
                "status" : recommend.status,
            })

        return {
            "message": "Get all recommends with products",
            "rows": result,
            "total": total
        }

    finally:
        session.close()

@router.get("/{recommend_id}")
def get_recommend(recommend_id: int):
    session = SessionLocal()
    
    try:

        recommend = session.query(RecommendSchema).join(ProductSchema,RecommendSchema.product_id == ProductSchema.id
        ).filter(RecommendSchema.id == recommend_id, ProductSchema.status != 'remove').first()
        
        if not recommend:
            raise HTTPException(status_code=404, detail="ไม่พบรายการสินค้าที่เเนะนำ")

        # Get product
        product = session.query(ProductSchema).filter(ProductSchema.id == recommend.product_id).first()

        # Get product image
        product_images = session.query(ProductImageSchema).filter(
            ProductImageSchema.product_id == product.id,
            ProductImageSchema.status == 'active'
        ).all()

        image_paths = [image.path for image in product_images]

        return {
            "message": "Get recommend by recommend_id: {recommend_id}",
            "row":{
                "product_id": recommend.product_id,
                "code": product.code,
                "name": product.name,
                "cost": product.cost,
                "price": product.price,
                "product_status": product.status,
                "category_id": product.category_id,
                "detail": product.detail,
                "images": image_paths,
                "start_date": recommend.start_date.strftime("%Y-%m-%d"),
                "end_date": recommend.end_date.strftime("%Y-%m-%d"),
                "status": recommend.status,
            } 
        }

    finally:
        session.close()

@router.put("/{recommend_id}")
def update_recommend(recommend_id: int, recommend: RecommendModel):
    session: Session = SessionLocal()
    try:
        existing_recommend = session.query(RecommendSchema).filter(RecommendSchema.id == recommend_id).first()

        if not existing_recommend:
            raise HTTPException(status_code=404, detail="ไม่พบข้อมูล")

        if recommend.product_id is not None:
            existing_recommend.product_id = recommend.product_id
        if recommend.start_date is not None:
            existing_recommend.start_date = recommend.start_date
        if recommend.end_date is not None:
            existing_recommend.end_date = recommend.end_date
        if recommend.status is not None:
            existing_recommend.status = recommend.status    

        updated_fields = {} 
        updated_fields = existing_recommend
        session.commit()

        return {
            "success": True,
            "message": "เเก้ไขข้อมูลสำเร็จ!",
            "id": recommend_id,
            "updated_data": updated_fields  
        }
    finally:
        session.close()

@router.post("/")
async def add_reccomend(recommend: RecommendModel):
    session = SessionLocal()
    try:

        # ตรวจสอบว่า product_id มีอยู่แล้วหรือไม่
        existing_recommend = session.query(RecommendSchema).filter(RecommendSchema.product_id == recommend.product_id).first()

        if existing_recommend:
            raise HTTPException(
                status_code=400,
                detail="สินค้านี้มีกำลังถูกเเนะนำอยู่"
            )
        
        new_recommend = RecommendSchema(
            product_id = recommend.product_id,
            start_date=recommend.start_date,
            end_date=recommend.end_date,
            status=recommend.status,
        )
        session.add(new_recommend)
        session.commit()  
        session.refresh(new_recommend)

        return {
            "success": True,
            "message": "บันทึกข้อมูลสำเร็จ",
            "updated_data": new_recommend
        }
    finally:
        session.close()

@router.delete("/{recommend_id}")
def remove_recommend(recommend_id: int):
    session: Session = SessionLocal()  #

    try:
        existing_recommend = session.query(RecommendSchema).filter(RecommendSchema.id == recommend_id).first()

        existing_recommend.status = "remove"

        # บันทึกการเปลี่ยนแปลง
        session.commit()

        # อัปเดตข้อมูลสินค้าและส่งกลับ
        session.refresh(existing_recommend)

        return {
            "success": True,
            "message": "อัปเดตสถานะเป็น remove สำเร็จ",
            "updated_data": existing_recommend
        }

    finally:
        session.close() 