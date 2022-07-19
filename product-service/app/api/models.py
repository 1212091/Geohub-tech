"""Model for product service"""

from pydantic import BaseModel

# pylint: disable=too-few-public-methods


class ProductIn(BaseModel):
    """Product input request class"""
    code: str
    name: str
    description: str
    price: int
    platform: str


class ProductOut(ProductIn):
    """Product output response class"""
    id: int
