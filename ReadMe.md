# How to use
## Route 1: Stock of coffee
### Go to /coffee_stock/kind of coffee you want to get
### For example, go to /coffee_stock/black (for black coffee)
If the coffee is in stock, you will get a set of {"type": "name of coffee", "stock": how many in stock(is an int), "ranking": the ranking (is an int)}

In this route, the first two datas would be useful.

If no coffee in stock matches your request, you will get a response of: {"msg": "Out of stock."}
## Route 2: Ranking of coffee
### Go to /coffee_ranking/ranking of coffee you want to get
### For example, go to /coffee_stock/1 (for 1 star quality)
If any coffee in stock matches your request ranking expectations, you will get a list of all the sets of {"type": "name of coffee", "stock": how many in stock(is an int), "ranking": the ranking (is an int)} of coffee that matches your expectations.

In this route, the first and third data would be useful, if the amount of stock is useful as well, it can be also included.

If no coffee in stock matches your request, you will get a response of: {"msg": "No coffee of this quality."}
