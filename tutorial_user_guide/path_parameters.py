#Path parameters
#You can declare path parameters or path variables with the same syntax used by python format string.

from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id):
    """A Path Operation Function with Path Parameter"""
    return {"item_id": item_id}

#path parameters with type
#You can declare the tpe of a path parameter in the function, using standard python type annotations.
@app.get("/books/{book_id}")
async def get_book(book_id: int):
    "Get a book by ID"
    return {"Book ID": book_id}

#Path converto
@app.get("/files/{file_id:path}")
async def read_fiel(file_id: str):
    return {"message": file_id}