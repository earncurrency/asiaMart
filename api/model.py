from pydantic import BaseModel

# Pydantic model โครงสร้างข้อมูล สำหรับการรับข้อมูลที่ต้องการอัปเดท
class MemberModel(BaseModel):
    code: str
    name: str
    phone: str
    status: str
    image: str

    class Config:
        orm_mode = True