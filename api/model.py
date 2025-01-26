from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# โมเดล Pydantic สำหรับข้อมูลสมาชิก
class MemberModel(BaseModel):
    code: Optional[str] = None
    name: Optional[str] = None
    phone: Optional[str] = None
    status: Optional[str] = None

# โมเดล Pydantic สำหรับข้อมูลสินค้า
class ProductModel(BaseModel):
    code: Optional[str] = None
    name: Optional[str] = None
    cost:Optional[float] = None
    price:Optional[float] = None
    status: Optional[str] = None
    category_id: Optional[int] = None
    detail: Optional[str] = None

# โมเดล Pydantic สำหรับข้อมูลรูปภาพสินค้า
class ProductImageModel(BaseModel):
    product_id: Optional[int] = None
    path: Optional[str] = None
    status: Optional[str] = None

# โมเดล Pydantic สำหรับประเภทสินค้า
class CategoryModel(BaseModel):
    name : Optional[str] = None
    status : Optional[str] = None

class OrderModel(BaseModel):
    code : Optional[str] = None
    order_date : Optional[datetime] = None
    member_id : Optional[int] = None
    address : Optional[str] = None
    total : Optional[float] = None
    status : Optional[str] = None
    length : Optional[int] = None

class OrderDetailModel(BaseModel):
    order_id: Optional[int] = None
    product_id: Optional[int] = None
    product_name: Optional[str] = None
    product_price:Optional[float] = None
    qty : Optional[int] = None

class Config:
    orm_mode = True
