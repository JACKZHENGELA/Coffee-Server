from fastapi import APIRouter

router_taste = APIRouter()


@router_taste.get("/")
async def get_all_tastes():
    return "List of all the tastes"


@router_taste.get("/{coffee_name}")
async def get_coffee_taste(coffee_name: str):
    return f"{coffee_name} has a great taste."
