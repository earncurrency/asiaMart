from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.future import select


# ข้อมูลการเชื่อมต่อกับฐานข้อมูล MySQL
DATABASE_URL = "mysql+mysqlconnector://root:150744@localhost/db_asiamart"

# สร้าง Engine และ SessionLocal
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

session = SessionLocal()
