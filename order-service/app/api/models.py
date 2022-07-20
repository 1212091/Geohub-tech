"""Model for order service"""

# pylint: disable=too-few-public-methods

from datetime import datetime
from typing import List

from pydantic import BaseModel, Field


class OrderItemIn(BaseModel):
    """Order item input request class"""
    product_id: int = Field(
        ...,
        title="id of product in the order",
        example="1",
    )
    quantity: int = Field(
        ...,
        title="quantity of product in the order",
        example="2",
    )


class OrderIn(BaseModel):
    """Order input request class"""
    user_id: int = Field(
        ...,
        title="User create this order (Call center people)",
        example="1",
    )
    order_user_id: int = Field(
        ...,
        title="User receive this order (usually customer)",
        example="2",
    )
    order_note: str = Field(
        ...,
        title="Note of the order",
        example="This order should be delivered in three days",
    )
    order_item_inputs: List[OrderItemIn]


class OrderOut(OrderIn):
    """Order output request class"""
    id: int = Field(
        ...,
        title="id of the order",
        example="1",
    )


class Order(BaseModel):
    """Order class to persist to database"""
    user_id: int = Field(
        ...,
        title="User create this order (Call center people)",
        example="1",
    )
    order_user_id: int = Field(
        ...,
        title="User receive this order (usually customer)",
        example="2",
    )
    order_date: datetime = Field(
        ...,
        title="Time that order is created",
        example="2022-01-19 03:14:07",
    )
    status: str = Field(
        ...,
        title="Status of the order",
        example="NEW",
    )
    notes: str = Field(
        ...,
        title="Note of the order",
        example="This order should be delivered in three days",
    )


class OrderItem(BaseModel):
    """Order item class to persist to database"""
    order_id: int = Field(
        ...,
        title="id of the order",
        example="1",
    )
    product_id: int = Field(
        ...,
        title="id of product in the order",
        example="1",
    )
    quantity: int = Field(
        ...,
        title="quantity of product in the order",
        example="2",
    )
