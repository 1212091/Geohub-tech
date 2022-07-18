from fastapi import APIRouter, HTTPException

import json
import os
import httpx

from typing import List, Union

from app.api.models import ProductOut, ProductIn
from app.api import db_manager
from app.api.utils import(
    create_action
)

products = APIRouter()

DEFAULT_SORT_BY = "code"

@products.post('/', response_model=ProductOut, status_code=201)
async def create_product(payload: ProductIn):
    product_id = await db_manager.add_product(payload)
    response = {
        'id': product_id,
        **payload.dict()
    }
    return response


@products.get('/', response_model=List[ProductOut])
async def get_products(
    user_id: int,
    sort_by: str=DEFAULT_SORT_BY,
    sort_asc: bool=False,
    filter_code: Union[str, None]=None,
    filter_name: Union[str, None]=None,
    filter_price: Union[int, None]=None,
    filter_platform: Union[str, None]=None
):
    action = create_action(sort_by, filter_code, filter_name, filter_price, filter_platform)
    user_activity_url = os.environ.get('USER_SERVICE_HOST_URL') + "activity"
    
    # We send user activity asynchronously to user service
    async with httpx.AsyncClient() as client:
        await client.post(
            user_activity_url,
            data=json.dumps({
                "user_id": user_id,
                "action": action
            })
        )
    
    products = await db_manager.get_products(
        sort_by,
        sort_asc,
        filter_code,
        filter_name,
        filter_price,
        filter_platform
    )
    return products


@products.get('/{id}/', response_model=ProductOut)
async def get_product(id: int):
    product = await db_manager.get_product(id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
