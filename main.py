from fastapi import FastAPI
import uvicorn
from routers.coffee_taste import router_taste
from routers.coffee_stock import router_stock
from routers.coffee_ranking import router_ranking

app = FastAPI()

app.include_router(router_taste, prefix="/coffee_taste")
app.include_router(router_stock, prefix="/coffee_stock")
app.include_router(router_ranking, prefix="/coffee_ranking")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)
