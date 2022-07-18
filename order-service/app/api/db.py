import os

from sqlalchemy import (Column, Integer, MetaData, String, Table, ForeignKey, DateTime, create_engine)

from databases import Database

DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
metadata = MetaData()

orders = Table(
    'orders',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer),
    Column('order_user_id', Integer),
    Column('order_date', DateTime),
    Column('status', String(10)),
    Column('notes', String(200))
)

order_items = Table(
    'order_items',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('order_id', Integer, foreign_keys=ForeignKey("orders.id")),
    Column('product_id', Integer),
    Column('quantity', Integer)
)

database = Database(DATABASE_URI)