"""Model for product service"""

from pydantic import BaseModel, Field

# pylint: disable=too-few-public-methods


class ProductIn(BaseModel):
    """Product input request class"""
    code: str = Field(
        ...,
        title="Product code",
        example="SMB",
    )
    name: str = Field(
        ...,
        title="Product name",
        example="Server message block",
    )
    description: str = Field(
        ...,
        title="Product description",
        example=("A network file sharing protocol that allows applications "
                 "on a computer to read and write to files and to request "
                 "services from server programs in a computer network")
    )
    price: int = Field(
        ...,
        title="Product price",
        example=50000,
    )
    platform: str = Field(
        ...,
        title="Platform that product can run on",
        example="Ubuntu"
    )


class ProductOut(ProductIn):
    """Product output response class"""
    id: int = Field(
        ...,
        title="Id of product",
        example=2,
    )
