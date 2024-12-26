from pydantic import BaseModel

# โมเดล Pydantic สำหรับข้อมูลสมาชิก
class MemberModel(BaseModel):
    code: str = None
    name: str = None
    phone: str = None
    status: str = None
    image: str = None


# โมเดล Pydantic สำหรับข้อมูลสินค้า
class ProductModel(BaseModel):
    code: str
    name: str
    status: str
    image: str

    class Config:
        orm_mode = True
