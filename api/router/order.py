from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc , func, extract
from datetime import datetime

from database import SessionLocal, engine
from model import OrderModel , OrderDetailModel ,ProductModel ,ProductImageModel
from schema import OrderSchema ,OrderDetailSchema ,ProductSchema ,ProductImageSchema

# สร้าง APIRouter สำหรับออเดอร์
router = APIRouter(
    prefix = "/orders",
    tags = ["orders"],
)

#เเสดง order ทั้งหมด
@router.get("/")
def list_orders(member_id: str = '', orders_status: str = '', limit: int = 10, offset: int = 0):
    """ List Orders """
    session = SessionLocal()
    try:

        query = session.query(OrderSchema).order_by(desc(OrderSchema.id))

        if member_id:
            query = query.filter(OrderSchema.member_id == member_id)

        if orders_status:
            query = query.filter(OrderSchema.status.notin_(['success', 'cancel']))


        orders = query.limit(limit).offset(offset).all()

        total = session.query(OrderSchema).filter(OrderSchema.status != 'remove').count()

        return {
            "message": "Get orders successfully",
            "rows": [
                {
                    "id": o.id,
                    "code": o.code,
                    "order_date": o.order_date.strftime("%Y-%m-%d %H:%M:%S"),
                    "member_id": o.member_id,
                    "member_name": o.member_name,
                    "member_phone": o.member_phone,
                    "address": o.address,
                    "total": o.total,
                    "status": o.status,
                    "length": o.length,
                } for o in orders
            ],
            "total": total
        }

    finally:
        session.close()

#บันทึก order
@router.post("/")
def add_order(order: OrderModel, orderDetails: list[OrderDetailModel]):
    session = SessionLocal()
    try:
        # เพิ่มออเดอร์หลัก (Order)
        new_order = OrderSchema(
            code=order.code,
            order_date=datetime.now(),
            member_id=order.member_id,
            member_name= order.member_name,
            member_phone= order.member_phone,
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
                product_name=detail.product_name,
                product_price=detail.product_price,
                qty=detail.qty,
            )
            session.add(new_order_detail)

        session.commit()

        # ส่งคืนข้อความการเพิ่มข้อมูลสำเร็จ
        return {"message": "เพิ่มออเดอร์สำเร็จ", "id": new_order.id}
    finally:
        session.close()

#เเสดงข้อมูลตาม order_id
@router.get("/{order_id}") 
def get_order(order_id: int):
    session = SessionLocal()
    try:
        # ดึงข้อมูลออเดอร์
        order = session.query(OrderSchema).filter(OrderSchema.id == order_id).first()

        if not order:
            raise HTTPException(status_code=404, detail="ไม่พบออเดอร์")

        # ฟอร์แมตวันที่ออเดอร์
        formatted_date = order.order_date.strftime("%Y-%m-%d %H:%M:%S")

        # ดึงรายละเอียดออเดอร์พร้อมผลิตภัณฑ์และรูปภาพที่เกี่ยวข้อง
        order_details = (
            session.query(OrderDetailSchema, ProductSchema)
            .join(ProductSchema, OrderDetailSchema.product_id == ProductSchema.id)
            .filter(OrderDetailSchema.order_id == order_id)
            .all()
        )

        products = []

        for detail, product in order_details:

            images = (
                session.query(ProductImageSchema)
                .filter(ProductImageSchema.product_id == product.id,ProductImageSchema.status == 'active')
                .first()
            )
            image_data = {}
            if images:
                image_data = {
                    "id": images.id,
                    "path": images.path
            }

            product_data = {
                "code": product.code,
                "id": product.id,
                "product_price": detail.product_price,
                "product_name": detail.product_name,
                "qty": detail.qty,
                "images": image_data
            }

            products.append(product_data)

        # เตรียมข้อมูลออเดอร์ที่จะส่งกลับ
        result = {
            "id": order.id,
            "code": order.code,
            "order_date": formatted_date,
            "member_id": order.member_id,
            "member_name": order.member_name,
            "member_phone": order.member_phone,
            "address": order.address,
            "total": order.total,
            "status": order.status,
            "length": order.length,
            "products": products
        }

        return {
            "message": "ดึงข้อมูลออเดอร์สำเร็จ",
            "row": result
        }

    finally:
        session.close()

@router.put("/{order_id}")
def update_order(order_id: int, order: OrderModel):
    session: Session = SessionLocal()
    try:
        existing_order = session.query(OrderSchema).filter(OrderSchema.id == order_id).first()

        if not existing_order:
            raise HTTPException(status_code=404, detail="ไม่พบข้อมูลออเดอร์")

        if order.status is not None:
            existing_order.status = order.status

        updated_fields = {} 
        updated_fields = existing_order
        session.commit()

        return {
            "success": True,
            "message": "เเก้ไขข้อมูลสำเร็จ!",
            "id": order_id,
            "updated_data": updated_fields  
        }
    finally:
        session.close()

