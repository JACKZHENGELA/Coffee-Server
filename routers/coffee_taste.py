from fastapi import APIRouter
from pydantic import BaseModel
import coffee_all
router_taste = APIRouter()




@router_taste.get("/")
async def get_all_tastes():
    return "List of all the tastes"

@router_taste.post("/")
async def add_new_coffee(type: type):
    coffee_all.append(type)
    return {"msg": "Coffee added"}

@router_taste.get("/{coffee_name}")
async def get_coffee_taste(coffee_name: str):
    for coffee in coffee_all:
        if coffee_name.lower() in coffee_all.type.lower():
            return coffee
    return {"msg": "Out of stock"}


