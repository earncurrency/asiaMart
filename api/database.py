from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.future import select
import socket

ip_address = socket.gethostbyname("localhost")

# ข้อมูลการเชื่อมต่อกับฐานข้อมูล MySQL
if ip_address=='192.168.4.12':
    DATABASE_URL = "mysql+mysqlconnector://root:@localhost/db_asiamart"
elif ip_address=='192.168.3.8':
    DATABASE_URL = "mysql+mysqlconnector://root:@localhost/db_asiamart"
else:
    DATABASE_URL = "mysql+mysqlconnector://root:password@localhost/db_asiamart"

# สร้าง Engine และ SessionLocal
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

session = SessionLocal()
