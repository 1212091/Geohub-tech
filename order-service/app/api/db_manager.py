"""Handle CRUD operation for order service"""

import datetime

from app.api.db import database, order_items, orders
from app.api.models import Order, OrderIn, OrderItem
from app.api.service import is_product_existed, is_user_existed, is_user_valid
from fastapi import HTTPException

NEW_STATUS = "NEW"


async def add_order(order_input: OrderIn):
    """Add a new order and order item to database"""
    validate_order_input(order_input)
    order = Order(
        user_id=order_input.user_id,
        order_user_id=order_input.order_user_id,
        order_date=datetime.datetime.now(),
        status=NEW_STATUS,
        notes=order_input.order_note
    )
    query = orders.insert().values(**order.dict())
    order_output = await database.execute(query=query)

    for order_item_input in order_input.order_item_inputs:
        order_item = OrderItem(
            order_id=order_output,
            product_id=order_item_input.product_id,
            quantity=order_item_input.quantity
        )
        query = order_items.insert().values(**order_item.dict())
        await database.execute(query=query)

    return order_output


def validate_order_input(order_input: OrderIn):
    """Validate order input from user"""
    if not is_user_existed(order_input.order_user_id):
        raise HTTPException(
            status_code=400,
            detail=f"User with given id: {order_input.order_user_id} is "
            "not existed"
        )
    if not is_user_existed(order_input.user_id):
        raise HTTPException(
            status_code=400,
            detail=f"User with given id: {order_input.user_id} is "
            "not existed"
        )
    if not is_user_valid(order_input.user_id):
        raise HTTPException(
            status_code=400,
            detail=f"User with given id: {order_input.user_id} is "
            "not Call Center"
        )

    for order_item_input in order_input.order_item_inputs:
        if not is_product_existed(order_item_input.product_id):
            raise HTTPException(
                status_code=400,
                detail=f"Product with given id: {order_item_input.product_id} "
                "is not existed"
            )
