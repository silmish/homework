from typing import List
from uuid import UUID
from fastapi import FastAPI, HTTPException, Request
from models import Order_products, OrderUpdateRequest, Orders, Product

app = FastAPI()

db_products: List[Product] = [
    Product(
        id=123,
        name="Ketchup",
        price="0.45"
    ),
    Product(
        id=456,
        name="Beer",
        price="2.33"
    ),
    Product(
        id=879,
        name="Õllesnäkk",
        price="0.42"
    ),
    Product(
        id=999,
        name="75\" OLED TV",
        price="1333.37"
    )
]
db_orders:  List[Orders] = []

@app.get("/api/products")
async def fetch_products():
    return db_products

@app.post("/api/orders")
async def create_order(order: Orders):
    db_orders.append(order)
    return {"id": order.id}

@app.get("/api/orders/{order_id}")
async def fetch_orders(order_id: UUID):
    for order in db_orders:
        if order.id == order_id:
            return order
    raise HTTPException(
        status_code = 404,
        detail=f"Order with id: {order_id} does not exist"
    )

@app.get("/api/orders/{order_id}/products")
async def get_order_products(order_id: UUID):
    for order in db_orders:
        if order.id == order_id:
            return order.products
    raise HTTPException(
        status_code = 404,
        detail=f"Order with id: {order_id} does not exist"
    )

@app.post("/api/orders/{order_id}/products", response_model=Order_products)
async def add_product_order(order_id: UUID, request: Request, order_product: Order_products):
    new_products = order_product.dict()
    for order in db_orders:
        if order.id == order_id:
            payload: dict = await request.json()
            new_products.update(payload)
            order.products.append(new_products)
            return
    raise HTTPException(
        status_code = 404,
        detail=f"Order with id: {order_id} does not exist"
    )

@app.patch("/api/orders/{order_id}")
async def update_order_info(order_update: OrderUpdateRequest, order_id: UUID):
    for order in db_orders:
        if order.id == order_id:
            if order_update.status is not None:
                order.status = order_update.status
                return order
    raise HTTPException(
        status_code = 404,
        detail=f"Order with id: {order_id} does not exist"
    )

@app.patch("/api/orders/{order_id}/products/{product_id}")
async def update_order_info(order_id: UUID, product_id: int, request: Request):
    payload = await request.json()
    for order in db_orders:
        if order.id == order_id:
            for product in order.products:  
                if product.id == product_id:
                    if "id" in payload:
                      product.id = payload["id"]
                      product.quantity = payload["quantity"]
                    else:
                        product.quantity = payload["quantity"]