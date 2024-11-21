#Pydantic Models - Pydantic is a python module for data validation
#you declare the shape of data as classes with attributes and and each attribute has a type
#then you create an instance of that class with some values and it will validate the values and convert them to appropriate types.
#Example
from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str = "Daniel Zadva"
    signup_ts: datetime | None = None
    friends: list[int] = []

external_data = {
    "id": 123,
    "signup_ts": "2017-06-01 12:24",
    "friends": [1, "2", b"3"]
}

user = User(**external_data)

print(user)
print(user.id)

