from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc, func, extract
from datetime import datetime

from database import SessionLocal, engine
from schema import OrderSchema, MemberSchema, ProductSchema

# สร้าง APIRouter สำหรับออเดอร์
router = APIRouter(
    prefix = "/report",
    tags = ["report"],
)

@router.get("/chart/")
def chart(year_month: str = ''):
    session = SessionLocal()
    try:
        # แยกเดือนและปีจาก year_month
        if year_month:
            year, month = map(int, year_month.split('/'))
        else:
            year, month = None, None

        # Query เพื่อ group by วัน เดือน และปี และคำนวณผลรวมของ total
        query = session.query(
            extract('year', OrderSchema.order_date).label('year'),
            extract('month', OrderSchema.order_date).label('month'),
            extract('day', OrderSchema.order_date).label('day'),
            func.sum(OrderSchema.total).label('total_sum')
        ).filter(
            OrderSchema.status == 'success'
        )

        # เพิ่มเงื่อนไขกรองตามเดือนและปีหาก year_month ถูกระบุ
        if month and year:
            query = query.filter(
                extract('month', OrderSchema.order_date) == month,
                extract('year', OrderSchema.order_date) == year
            )

        results = query.group_by(
            extract('year', OrderSchema.order_date),
            extract('month', OrderSchema.order_date),
            extract('day', OrderSchema.order_date)
        ).order_by(
            extract('year', OrderSchema.order_date),
            extract('month', OrderSchema.order_date),
            extract('day', OrderSchema.order_date)
        ).all()

        # แปลงผลลัพธ์ให้อยู่ในรูปแบบที่ต้องการ
        chart_data = [{
            'day_month_year': f"{result.year}/{str(result.month).zfill(2)}/{str(result.day).zfill(2)}",
            'total_sum': result.total_sum
        } for result in results]

        return {
            "message": "Get daily totals successfully",
            "rows": chart_data,
            "total": len(chart_data),
        }

    finally:
        session.close()