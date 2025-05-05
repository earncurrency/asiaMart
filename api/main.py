# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from router import member
from router import product
from router import category
from router import order
from router import admin
from router import dashboard
from router import recommend
from router import report
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

app.include_router(member.router)
app.include_router(product.router)
app.include_router(category.router)
app.include_router(order.router)
app.include_router(admin.router)
app.include_router(dashboard.router)
app.include_router(recommend.router)
app.include_router(report.router)

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


