#First steps
#Simple fast api file
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

#in development environment you can use 
# fastapi dev first_steps.py

#you check your api served at
#1. http://127.0.0.1:8000
#2. Interractive doc at http://127.0.0.1:8000/docs
#3. Alternative doc at http://127.0..0.1:8000/redoc
#4. API Schema at http://127.0.0.1:8000/openapi.doc