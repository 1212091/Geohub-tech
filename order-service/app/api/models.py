"""Model for order service"""

# pylint: disable=too-few-public-methods

from datetime import datetime
from typing import List

from pydantic import BaseModel


class OrderItemIn(BaseModel):
    """Order item input request class"""
    product_id: int
    quantity: int


class OrderIn(BaseModel):
    """Order input request class"""
    user_id: int  # User create this order
    order_user_id: int  # User will receive this order
    order_note: str
    order_item_inputs: List[OrderItemIn]


class OrderOut(OrderIn):
    """Order output request class"""
    id: int


class Order(BaseModel):
    """Order class to persist to database"""
    user_id: int
    order_user_id: int
    order_date: datetime
    status: str
    notes: str


class OrderItem(BaseModel):
    """Order item class to persist to database"""
    order_id: int
    product_id: int
    quantity: int
