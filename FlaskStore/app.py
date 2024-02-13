from typing import TypedDict,List
from flask import Flask,request
app = Flask(__name__)

class Item(TypedDict):
    name: str
    price: float

class Store(TypedDict):
    name:str
    items:List[Item]

stores:List[Store] = [
    {
        "name": "Grocery Store",
        "items": [
            {"name": "Apples", "price": 1.99},
            {"name": "Bananas", "price": 0.99},
            {"name": "Milk", "price": 2.49}
        ]
    },
    {
        "name": "Electronics Store",
        "items": [
            {"name": "Laptop", "price": 999.99},
            {"name": "Smartphone", "price": 699.99},
            {"name": "Headphones", "price": 49.99}
        ]
    },
    {
        "name": "Clothing Store",
        "items": [
            {"name": "T-Shirt", "price": 19.99},
            {"name": "Jeans", "price": 39.99},
            {"name": "Sneakers", "price": 59.99}
        ]
    }
]


@app.get('/store')
def get_stores():
    return {"stores":stores}

@app.post('/store')
def create_store():
    request_data = request.get_json()
    new_store = {'name':request_data['name'],'items':[]}
    stores.append(new_store)
    return new_store,201

@app.post('/store/<string:name>/item')
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item:Item = {'name':request_data['name'],
                             'price':request_data['price']}
            store['items'].append(new_item)
            return new_item,201
    return {'message':'Store not found'},404

@app.get('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return store,201
    return {'message':'Store not found'},404

@app.get('/store/<string:name>/item')
def get_items(name):
    for store in stores:
        if store['name'] == name:
            return {'items':store["items"]},201
    return {'message':'Store not found'},404


if __name__ =='__main__':
    app.run(debug=True)
