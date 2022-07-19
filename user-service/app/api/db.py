"""Database objects for user service"""

import os

from databases import Database
from sqlalchemy import (Column, DateTime, ForeignKey, Integer, MetaData,
                        String, Table, create_engine)

DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
metadata = MetaData()

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('first_name', String(50)),
    Column('last_name', String(50)),
    Column('phone', String(20)),
    Column('email', String(40)),
    Column('address', String(100)),
    Column('role_id', Integer, foreign_keys=ForeignKey("user_role.id"))
)

user_role = Table(
    'user_role',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('role_name', String(20))
)

user_activity = Table(
    'user_activity',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, foreign_keys=ForeignKey("users.id")),
    Column('action', String(500)),
    Column('timestamp', DateTime)
)
database = Database(DATABASE_URI)
