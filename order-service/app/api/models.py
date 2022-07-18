from datetime import datetime
from pydantic import BaseModel
from typing import List

class OrderItemIn(BaseModel):
    product_id: int
    quantity: int


class OrderIn(BaseModel):
    user_id: int # User create this order
    order_user_id: int # User will receive this order
    order_note: str
    order_item_inputs: List[OrderItemIn]


class OrderOut(OrderIn):
    id: int
    

class Order(BaseModel):
    user_id: int
    order_user_id: int
    order_date: datetime
    status: str
    notes: str


class OrderItem(BaseModel):
    order_id: int
    product_id: int
    quantity: int