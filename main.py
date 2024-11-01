from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "Hello World!"
    }

#Path parameters
#You can delcare path parameter or variable with the same syntax used by python
#strings
@app.get("/items/{item_id}")
async def get_item(item_id):
    return { "item_id": item_id }
#the value of the path parameter item_id will be passed to your function as argument item_id.
#for example if you run this example and go to http://127.0.0.1:8000/items/foo you will get a response:
# of { "item_id": "foo" }


#Path parameters with type
#You can declare the type of path parameters in the function using python standard type annotations
@app.get("/books/{book_id}")
async def get_book(book_id: int) -> dict:
    return {
        "book_id": book_id
    }
