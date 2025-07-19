from fastapi import APIRouter
from app.models.order import OrderIn, OrderOut
from app.db import db
from bson import ObjectId

router = APIRouter()

@router.post("/", response_model=OrderOut, status_code=201)
async def create_order(order: OrderIn):
    doc = order.dict()
    result = await db.orders.insert_one(doc)
    return {"id": str(result.inserted_id)}


@router.get("/{user_id}")
async def get_orders(user_id: str, limit: int = 10, offset: int = 0):
    cursor = db.orders.find({"userId": user_id}).skip(offset).limit(limit)
    orders = []
    async for doc in cursor:
        items = []
        for item in doc["items"]:
            product = await db.products.find_one({"_id": ObjectId(item["productId"])});
            items.append({
                "productDetails": {
                    "id": item["productId"],
                    "name": product["name"] if product else "Unknown"
                },
                "qty": item["qty"]
            })

        orders.append({
            "id": str(doc["_id"]),
            "items": items,
            "total": sum([i["qty"] * 100 for i in doc["items"]])
        })

    return {
        "data": orders,
        "page": {
            "next": str(offset + limit),
            "limit": limit,
            "previous": str(offset - limit)
        }
    }
