""" Doc String. """
# from sqlalchemy import Column, ForeignKey, Integer, String, Numeric, DateTime, ForeignKey, CHAR, Table
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:password@localhost:3306/asiagroup_app"
# # SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://root:password@localhost:3306/db"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

import sqlalchemy as db
from sqlalchemy.orm import Session
engine = db.create_engine('mysql+mysqlconnector://root:@localhost:3306/asiagroup_app')

connection = engine.connect()
metadata = db.MetaData()
# connection.execute('SET GLOBAL connect_timeout='+str(10))
connection.execute('SET GLOBAL wait_timeout='+str(60*10))
connection.execute('SET GLOBAL interactive_timeout='+str(60))
print("- sqlAlchemy Connected")

def get_db():
    dbSession = Session(engine)
    try:
        yield dbSession
    finally:
        dbSession.close()
