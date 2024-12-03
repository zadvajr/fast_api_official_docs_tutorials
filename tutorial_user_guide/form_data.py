#when you need to receive form fields instead of json, you can make use of Form
#To use Form you need to first install python-multipart
#data from form is encoded as application/x-www-form-urlencoded
#but when the form includes file, it is encoded as multipart/form-data
from typing import Annotated
from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username, "password": password}