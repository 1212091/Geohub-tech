import os

from sqlalchemy import (Column, DateTime, Integer, BigInteger, MetaData, String, Table,
                        create_engine, ARRAY)

from databases import Database

DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
metadata = MetaData()

products = Table(
    'products',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('code', String(10)),
    Column('name', String(50)),
    Column('description', String(250)),
    Column('price', BigInteger),
    Column('platform', String(50))
)

database = Database(DATABASE_URI)