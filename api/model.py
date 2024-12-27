from pydantic import BaseModel
from typing import Optional

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
    cost:Optional[str] = None
    sell:Optional[str] = None
    status: Optional[str] = None

class Config:
    orm_mode = True
