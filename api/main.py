from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector, os

def get_db_connection():
    cnx = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "150744",
        database = "db_crm",
    )
    return cnx

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
    cnx = get_db_connection()
    cursor = cnx.cursor()
    query = "SELECT * FROM tb_member"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    cnx.close()

    return rows


@app.get('/')
def read_root():
    return {"msg" : "test"}
