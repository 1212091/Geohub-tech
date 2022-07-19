"""Handle CRUD operation for product service"""

#pylint: disable=too-many-arguments

from typing import Union

from app.api.db import database, engine, products
from app.api.models import ProductIn
from sqlalchemy import asc, desc
from sqlalchemy.orm import Session


async def add_product(payload: ProductIn):
    """Insert a single product to database"""
    query = products.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_product(product_id: int):
    """Get a single product from database by id"""
    query = products.select(products.c.id == product_id)
    return await database.fetch_one(query=query)


async def get_products(
    sort_by: str,
    sort_asc: bool,
    filter_code: Union[str, None] = None,
    filter_name: Union[str, None] = None,
    filter_price: Union[int, None] = None,
    filter_platform: Union[str, None] = None
):
    """Get all products based on some filters and sort"""
    with Session(engine) as session:
        query = session.query(products)
        if filter_code:
            query = query.filter(products.c.code.like(filter_code + "%"))
        if filter_name:
            query = query.filter(products.c.name.like(filter_name + "%"))
        if filter_price:
            query = query.filter(products.c.price >= filter_price)
        if filter_platform:
            query = query.filter(
                products.c.platform.like(filter_platform + "%")
            )
        if sort_asc:
            query = query.order_by(asc(sort_by))
        else:
            query = query.order_by(desc(sort_by))
    return query.all()
