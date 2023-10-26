from pydantic import BaseModel
class Coffee(BaseModel):
    type: str
    stock: int
    ranking: int
    taste_good: bool | None = False

coffee_all = [
    Coffee(type="cappuccino", stock=1, ranking=1),
    Coffee(type="espresso", stock=2, ranking=5),
    Coffee(type="caffè mocha", stock=3, ranking=3),
    Coffee(type="latte", stock=4, ranking=1),
    Coffee(type="americano", stock=5, ranking=2),
    Coffee(type="flat white", stock=6, ranking=8),
    Coffee(type="caffè macchiato", stock=7, ranking=1),
    Coffee(type="cortado", stock=8, ranking=4),
    Coffee(type="café au lait", stock=9, ranking=1),
    Coffee(type="cold brew", stock=10, ranking=6),
    Coffee(type="iced coffee", stock=11, ranking=8),
    Coffee(type="irish coffee", stock=12, ranking=7),
    Coffee(type="ristretto", stock=13, ranking=4),
    Coffee(type="frappe", stock=14, ranking=1),
    Coffee(type="doppio", stock=15, ranking=1),
    Coffee(type="coffea arabica", stock=16, ranking=2),
    Coffee(type="lungo", stock=17, ranking=4),
    Coffee(type="red Eye", stock=18, ranking=3),
    Coffee(type="long red", stock=19, ranking=1),
    Coffee(type="black", stock=20, ranking=9),
]
