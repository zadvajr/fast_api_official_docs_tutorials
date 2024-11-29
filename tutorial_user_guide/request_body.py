#Request body
#When you need to send data from your client, let's say a browser to your API
#you make use of request body.
#Request body is a data sent to your API by the client.
#Response body on the other hand is a data sent to client by your API

#Your API almost always has to send a response body. But client don't necessarily 
# need to send a request body all of the time
#Sometime they only request a path with some query parameters but don't send a body.

#To declare a request body you make use of pydantic models with all their power and benefits.
#To send data you should make use of one of POST(the most common), PUT, DELETE, PATCH

from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid1

app = FastAPI()

item_db = []

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post('/items/', status_code=201)
async def create_item(item: Item):
    item['id'] = uuid1()
    item_db.append(item)
    return {"message": "Item added successfully"}

@app.get('/items/')
async def get_items():
    return item_db