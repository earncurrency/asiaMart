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
    prefix = "/recommend",
    tags = ["recommend"],
)

@router.get("/")
def get_reccomend(limit: int = 10, q: str = '', page: int = 1):  
    session = SessionLocal()

    offset = (page * limit) - limit

    try:

        query = session.query(ProductSchema).filter(ProductSchema.id == RecommendSchema.product_id ,ProductSchema.status != 'remove')

        if q:
            query = query.filter(ProductSchema.name.ilike(f'%{q}%'))

        products = query.order_by(desc(ProductSchema.id)).limit(limit).offset(offset).all()

        total = query.count()

        # สร้างผลลัพธ์ที่ต้องการส่งกลับ
        result = []
        for product in products:

            recommend = session.query(RecommendSchema).filter(
                RecommendSchema.product_id == product.id
            ).first()
            start_date = recommend.start_date if recommend else None
            end_date = recommend.end_date if recommend else None

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
                "images": image_paths ,
                "start_date": start_date.strftime("%Y-%m-%d %H:%M:%S"),  
                "end_date": end_date.strftime("%Y-%m-%d %H:%M:%S") ,
            })

        return {
            "message": "Get active products by recommend",
            "rows": result,
            "total": total
        }

    finally:
        session.close()
