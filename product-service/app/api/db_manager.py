from app.api.models import ProductIn
from app.api.db import products, database, engine
from typing import Union
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc


async def add_product(payload: ProductIn):
    query = products.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_product(id):
    query = products.select(products.c.id==id)
    return await database.fetch_one(query=query)


async def get_products(
    sort_by: str,
    sort_asc: bool,
    filter_code: Union[str, None]=None,
    filter_name: Union[str, None]=None,
    filter_price: Union[int, None]=None,
    filter_platform: Union[str, None]=None
):
    with Session(engine) as session:
        query = session.query(products)
        if filter_code:
            query = query.filter(products.c.code.like(filter_code + "%"))
        if filter_name:
            query = query.filter(products.c.name.like(filter_name + "%"))
        if filter_price:
            query = query.filter(products.c.price >= filter_price)
        if filter_platform:
            query = query.filter(products.c.platform.like(filter_platform + "%"))
        if sort_asc:
            query = query.order_by(asc(sort_by))
        else:
            query = query.order_by(desc(sort_by))
    return query.all()

        
    