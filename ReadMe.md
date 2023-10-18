# Coffee API
### This API keeps track of all coffee stock and coffee rankings. You can use the API to find out whether or not a type of coffee is in stock and if so, how much, also, it can find out all the types of coffee at your desired ranking.
In order to access these routes, you need to use an api key. For all requests, you can use the api key as a query paramter with the key and value pair of :
```python
API_KEYS = ["071113", "a8kl7dfj"]
```
### Get stock of coffee
Example Path: 
``````
10.6.20.239/coffee_stock/black?api_key= {API_KEY}
``````
Result: 
``````
{"type":"long black","stock":19,"ranking":1}
``````
### Get ranking of coffee
Example Path:
``````
10.6.20.239/coffee_ranking/1?api_key= {API_KEY}
``````
Result:
``````
[{"type":"cappuccino","stock":1,"ranking":1},{"type":"latte","stock":4,"ranking":1},{"type":"caff猫 macchiato","stock":7,"ranking":1},{"type":"caf茅 au lait","stock":9,"ranking":1},{"type":"frappe","stock":14,"ranking":1},{"type":"doppio","stock":15,"ranking":1},{"type":"long black","stock":19,"ranking":1}]
``````