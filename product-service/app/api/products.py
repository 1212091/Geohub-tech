"""Controller to handle request for product service"""

#pylint: disable=too-many-arguments

from typing import List, Optional, Union

from app.api import db_manager
from app.api.models import ProductIn, ProductOut
from app.api.service import save_user_activity
from fastapi import APIRouter, HTTPException, Path, Query

products = APIRouter()

# Default sort by when view product
DEFAULT_SORT_BY = "code"


@products.post(
    '/',
    summary="Create a new product",
    response_model=ProductOut,
    status_code=201
)
async def create_product(payload: ProductIn):
    """Create a new product"""
    product_id = await db_manager.add_product(payload)
    response = {
        'id': product_id,
        **payload.dict()
    }
    return response


@products.get(
    '/',
    summary=(
        "Get a list of products. Users can filter or sort by some fields."
    ),
    response_model=List[ProductOut]
)
async def get_products(
    user_id: int = Query(
        ..., description="Returns UI constructor parameters if True"
    ),
    sort_by: str = Query(
        DEFAULT_SORT_BY,
        description="Input field response can be sorted by"
    ),
    sort_asc: bool = Query(
        False,
        description="Sort value ascending or descending"
    ),
    filter_code: Optional[str] = Query(
        None,
        description="Filter result by code"
    ),
    filter_name: Optional[str] = Query(
        None,
        description="Filter result by product name"
    ),
    filter_price: Optional[int] = Query(
        None,
        description="Filter result by product price"
    ),
    filter_platform: Optional[int] = Query(
        None,
        description="Filter result by product platform"
    )
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


@products.get(
    '/{product_id}/',
    summary="Get product by id",
    response_model=ProductOut
)
async def get_product(
    product_id: int = Path(
        ..., description="id of product"
    ),
):
    """Get a product by id"""
    product = await db_manager.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
