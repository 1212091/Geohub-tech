"""Controller to handle request for product service"""

#pylint: disable=too-many-arguments

from typing import List, Union

from app.api import db_manager
from app.api.models import ProductIn, ProductOut
from app.api.service import save_user_activity
from fastapi import APIRouter, HTTPException

products = APIRouter()

# Default sort by when view product
DEFAULT_SORT_BY = "code"


@products.post('/', response_model=ProductOut, status_code=201)
async def create_product(payload: ProductIn):
    """Create a new product"""
    product_id = await db_manager.add_product(payload)
    response = {
        'id': product_id,
        **payload.dict()
    }
    return response


@products.get('/', response_model=List[ProductOut])
async def get_products(
    user_id: int,
    sort_by: str = DEFAULT_SORT_BY,
    sort_asc: bool = False,
    filter_code: Union[str, None] = None,
    filter_name: Union[str, None] = None,
    filter_price: Union[int, None] = None,
    filter_platform: Union[str, None] = None
):
    """Get a list of product with some filter and sort"""
    await save_user_activity(
        user_id,
        sort_by,
        sort_asc,
        filter_code,
        filter_name,
        filter_price,
        filter_platform
    )
    list_product = await db_manager.get_products(
        sort_by,
        sort_asc,
        filter_code,
        filter_name,
        filter_price,
        filter_platform
    )
    return list_product


@products.get('/{product_id}/', response_model=ProductOut)
async def get_product(product_id: int):
    """Get a product by id"""
    product = await db_manager.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
