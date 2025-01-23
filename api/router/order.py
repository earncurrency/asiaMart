from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
from datetime import datetime

from database import SessionLocal, engine
from model import OrderModel , OrderDetailModel
from schema import OrderSchema ,OrderDetailSchema

# สร้าง APIRouter สำหรับออเดอร์
router = APIRouter(
    prefix = "/orders",
    tags = ["orders"],
)

@router.get("/")
def list_orders():
    session = SessionLocal()
    try:
        # ทำการ query ข้อมูลจาก OrderSchema และ OrderDetailSchema
        orders = session.query(OrderSchema).order_by(desc(OrderSchema.id)).all()

        # สร้างผลลัพธ์ที่จะส่งกลับ
        result = []
        for order in orders:
            
            formatted_date = order.date.strftime("%Y-%m-%d %H:%M:%S")

            # ดึงข้อมูลรายละเอียดของแต่ละออเดอร์
            order_details = session.query(OrderDetailSchema).filter(OrderDetailSchema.order_id == order.id).all()

            # สร้างรายการรายละเอียดออเดอร์
            details = [
                {
                    "product_id": detail.product_id,
                    "qty": detail.qty
                }
                for detail in order_details
            ]
            result.append({
                "id": order.id,
                "code": order.code,
                "date": formatted_date,
                "member_id": order.member_id,
                "address": order.address,
                "total": order.total,
                "status": order.status,
                "length": order.length,
                "details": details  # ส่งข้อมูลรายละเอียดของออเดอร์ทั้งหมด
            })

        return {
            "message": "Get orders successfully",
            "rows": result,
            "total": len(result)
        }

    finally:
        session.close()



@router.post("/")
def add_order(order: OrderModel, orderDetails: list[OrderDetailModel]):
    session = SessionLocal()
    try:
        # เพิ่มออเดอร์หลัก (Order)
        new_order = OrderSchema(
            code=order.code,
            date=datetime.now(),
            member_id=order.member_id,
            address=order.address,
            total=order.total,
            status=order.status,
            length=order.length,
        )

        session.add(new_order)
        session.commit()

        # เพิ่มข้อมูลรายละเอียดของออเดอร์ (Order Details)
        for detail in orderDetails:
            new_order_detail = OrderDetailSchema(
                order_id=new_order.id,
                product_id=detail.product_id,
                qty=detail.qty,
            )
            session.add(new_order_detail)

        session.commit()

        # ส่งคืนข้อความการเพิ่มข้อมูลสำเร็จ
        return {"message": "เพิ่มออเดอร์สำเร็จ", "id": new_order.id}
    finally:
        session.close()

