from fastapi import APIRouter
from coffee_all import coffee_all
from APP_KEY import API_KEYS

router_ranking = APIRouter()


@router_ranking.get("/{ranking}")
async def get_coffee_list(ranking: int, api_key: str):
    if api_key in API_KEYS:
        ranking_ls = []
        for coffee in coffee_all:
            if int(ranking) == coffee["ranking"]:
                ranking_ls.append(coffee)
        if ranking_ls != []:
            return (ranking_ls)
        return {"msg": "No coffee of this quality."}
    return {"msg": "Get outta here you don't have access"}
