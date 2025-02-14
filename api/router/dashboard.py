from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc , func, extract
from datetime import datetime

from database import SessionLocal, engine
from schema import OrderSchema , MemberSchema, ProductSchema

# สร้าง APIRouter สำหรับออเดอร์
router = APIRouter(
    prefix = "/dashboard",
    tags = ["dashboard"],
)

@router.get("/chart/")
def chart():
    session = SessionLocal()
    try:
        # Query เพื่อ group by เดือนและปี และคำนวณผลรวมของ total
        results = session.query(
            extract('year', OrderSchema.order_date).label('year'),
            extract('month', OrderSchema.order_date).label('month'),
            func.sum(OrderSchema.total).label('total_sum')
        ).filter(
            OrderSchema.status == 'success'  
        ).group_by(
            extract('year', OrderSchema.order_date),
            extract('month', OrderSchema.order_date)
        ).order_by(
            extract('year', OrderSchema.order_date),
            extract('month', OrderSchema.order_date)
        ).all()

        # แปลงผลลัพธ์ให้อยู่ในรูปแบบที่ต้องการ
        chart_data = [{
            'month_year': f"{str(result.month).zfill(2)}/{result.year}",
            'total_sum': result.total_sum
        } for result in results]

        return {
            "message": "Get monthly totals successfully",
            "rows": chart_data,
            "total": len(chart_data),
        }

    finally:
        session.close()

#เเสดง order ทั้งหมด
@router.get("/total/")
def total():

    session = SessionLocal()
    try:
        order = session.query(OrderSchema).count()
        member = session.query(MemberSchema).count()
        product = session.query(ProductSchema).filter(ProductSchema.status != 'remove').count()

        results = session.query(func.sum(OrderSchema.total).label('total_sum')).filter(OrderSchema.status == 'success').all()
        total_sales = sum(result.total_sum or 0 for result in results) 

        return {
            "order": order,
            "member" : member,
            "product" : product,
            "total_sales" : total_sales,
        }
    finally:
        session.close()
