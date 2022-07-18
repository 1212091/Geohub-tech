from fastapi import APIRouter
from app.api.models import OrderOut, OrderIn
from app.api import db_manager

orders = APIRouter()


@orders.post('/', response_model=OrderOut, status_code=201)
async def create_order(order_input: OrderIn):
    order_id = await db_manager.add_order(order_input)
    response = {
        'id': order_id,
        **order_input.dict()
    }
    return response