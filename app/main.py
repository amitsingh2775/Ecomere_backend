from fastapi import FastAPI
from app.routes import product, order

app = FastAPI()

app.include_router(product.router, prefix="/products", tags=["Products"])
app.include_router(order.router, prefix="/orders", tags=["Orders"])
