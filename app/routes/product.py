from fastapi import APIRouter, Query
from app.models.product import ProductIn, ProductOut
from app.db import db

router = APIRouter()

@router.post("/", response_model=ProductOut, status_code=201)
async def create_product(product: ProductIn):
    doc = product.dict()
    result = await db.products.insert_one(doc)
    return {"id": str(result.inserted_id)}


@router.get("/")
async def list_products(
    name: str = None,
    size: str = None,
    limit: int = 10,
    offset: int = 0
):
    query = {}
    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    if size:
        query["sizes.size"] = size

    cursor = db.products.find(query).skip(offset).limit(limit)
    products = []
    async for doc in cursor:
        products.append({
            "id": str(doc["_id"]),
            "name": doc["name"],
            "price": doc["price"]
        })

    return {
        "data": products,
        "page": {
            "next": str(offset + limit),
            "limit": limit,
            "previous": str(offset - limit)
        }
    }

