from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from database import connection, get_db

# import mysql.connector
# def get_db_connection():
#     cnx = mysql.connector.connect(
#         host = "localhost",
#         user = "root",
#         password = "150744",
#         database = "db_crm",
#     )
#     return cnx

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/members')
def get_member():
    sql = """
        select * from tb_employee limit 10
    """
    result = connection.execute(sql).fetchall()

    sql = """
        select count(id) as total from tb_employee
    """
    total = connection.execute(sql).fetchone()

    return {'total':total, 'rows':result}


@app.get('/')
def read_root():
    return {"msg" : "test"}

