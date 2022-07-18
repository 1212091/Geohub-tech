from pydantic import BaseModel
from typing import List

class ProductIn(BaseModel):
    code: str
    name: str
    description: str
    price: int
    platform: str
    
class ProductOut(ProductIn):
    id: int