# Construct ORM from PostgreSQL Database with SQLAlchemy and Python

# Let's say we have a postgresl and a table, named 'table' with a structure as follows :

#   id = Column(String, primary_key=True)
#   item_id = Column(String)
#   created_at = Column(String)
#   json_data = Column(JSONB)

import sqlalchemy
from sqlalchemy import Column, String 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.dialects.postgresql import JSONB
import psycopg2
 
user = 'username'
password = 'password'
address = 'address'
database = 'database'
 
db = create_engine(f'postgresql://{user}:{password}@{address}/{database}')
base = declarative_base()
 
class Table(base): 
    __tablename__ = 'table'
    id = Column(String, primary_key=True)
    item_id = Column(String)
    created_at = Column(String)
    json_data = Column(JSONB)
     
Session = sessionmaker(db) 
session = Session()
base.metadata.create_all(db)