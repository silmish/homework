from distutils.command.build_scripts import first_line_re
from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel

class Order_products(BaseModel):
    id: int
    quantity = 1

class Product(BaseModel):
    id: int
    name: str
    price: str

class Orders(BaseModel):
    id: Optional[UUID] = uuid4()
    status = "Unpaid"
    products: Optional[List[Order_products]]

class OrderUpdateRequest(BaseModel):
    status: Optional[str]
    products: Optional[List[Order_products]]
    