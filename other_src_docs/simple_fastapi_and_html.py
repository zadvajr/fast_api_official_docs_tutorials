from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Testing FastAPI with HTML</title>
    </head>
    <body>
        <h1>Welcome to my FastAPI Application with HTML</h1><hr>
        <p>This html page is built with fastapi and html using HTMLResponse from fastapi</p>
    </body>
</html>
"""

@app.get("/")
async def home():
    return HTMLResponse(html)