from fastapi import APIRouter
from coffee_all import coffee_all
from APP_KEY import API_KEYS

router_stock = APIRouter()


@router_stock.get("/{coffee_kind}")
async def get_profile(coffee_kind: str, api_key: str):
    if api_key in API_KEYS:
        for coffee in coffee_all:
            if coffee_kind.lower() in coffee["type"].lower():
                return coffee
        return {"msg": "Out of stock."}
    return {"msg": "Get outta here you don't have access"}
