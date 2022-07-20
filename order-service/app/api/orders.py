"""Controller to handle request for order service"""

from app.api import db_manager
from app.api.models import OrderIn, OrderOut
from fastapi import APIRouter

orders = APIRouter()


@orders.post(
    '/',
    summary="Create a new order",
    response_model=OrderOut,
    status_code=201
)
async def create_order(order_input: OrderIn):
    """Create a new order"""
    order_id = await db_manager.add_order(order_input)
    response = {
        'id': order_id,
        **order_input.dict()
    }
    return response
