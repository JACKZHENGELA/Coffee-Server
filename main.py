from fastapi import FastAPI

import uvicorn


app = FastAPI()
API_KEYS = ["071113", "a8kl7dfj"]

coffee_all = [
    {"type": "cappuccino", "stock": 1, "ranking": 1},
    {"type": "espresso", "stock": 2, "ranking": 5},
    {"type": "caffè mocha", "stock": 3, "ranking": 3},
    {"type": "latte", "stock": 4, "ranking": 1},
    {"type": "americano", "stock": 5, "ranking": 2},
    {"type": "flat white", "stock": 6, "ranking": 8},
    {"type": "caffè macchiato", "stock": 7, "ranking": 1},
    {"type": "cortado", "stock": 8, "ranking": 4},
    {"type": "café au lait", "stock": 9, "ranking": 1},
    {"type": "cold brew", "stock": 10, "ranking": 6},
    {"type": "iced coffee", "stock": 11, "ranking": 8},
    {"type": "irish coffee", "stock": 12, "ranking": 7},
    {"type": "ristretto", "stock": 13, "ranking": 4},
    {"type": "frappe", "stock": 14, "ranking": 1},
    {"type": "doppio", "stock": 15, "ranking": 1},
    {"type": "coffea arabica", "stock": 16, "ranking": 2},
    {"type": "lungo", "stock": 17, "ranking": 4},
    {"type": "red Eye", "stock": 18, "ranking": 3},
    {"type": "long black", "stock": 19, "ranking": 1},
    {"type": "black", "stock": 20, "ranking": 9},
]


@app.get("/coffee_stock/{coffee_kind}")
async def get_profile(coffee_kind: str, api_key: str):
    if api_key in API_KEYS:
        for coffee in coffee_all:
            if coffee_kind.lower() in coffee["type"].lower():
                return coffee
        return {"msg": "Out of stock."}
    return {"msg": "Get outta here you don't have access"}

@app.get("/coffee_ranking/{ranking}")
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



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)
