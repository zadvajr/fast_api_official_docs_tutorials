#You can use pydantic models to to declare form fields in fastapi

#Pydantic models for forms
from typing import Annotated
from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()

class FormData(BaseModel):
    username: str
    password: str

@app.post("/login/")
async def login(data: Annotated[FormData, Form()]):
    return data

#You can use python pydantic model to forbid extra fields as follows

class LoginUser(BaseModel):
    email: str
    pass: str
    model_config = {"extra": "forbid"}

@app.post("/user/login")
async def login_user(data: Annotated[LoginUser, Form()]):
    return data