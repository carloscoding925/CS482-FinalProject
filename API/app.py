# Carlos Hernandez & Jonathan Nunez

from fastapi import FastAPI

app = FastAPI()

# Sample endpoint to test in remix app
@app.get("/hello")
def read_root():
    return {"Hello": "World"}

# Sample async function
@app.get("/sample")
async def read_item():
    return {"Hello": "World"}