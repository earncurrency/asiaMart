# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from router import member
from router import product
from router import category
from router import order
# from router import product_image

# สร้างแอปพลิเคชัน FastAPI
app = FastAPI()

# ตั้งค่า CORS
origins = [
    "*",
    # "http://*",
    # "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# รวม Router สำหรับสมาชิก
app.include_router(member.router)
app.include_router(product.router)
app.include_router(category.router)
app.include_router(order.router)
# app.include_router(product_image.router)
