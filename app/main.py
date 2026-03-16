from app import api
from fastapi import FastAPI
from app.api.v1.router import api_router

app = FastAPI(title="YT FastAPI Project")

@app.get("/") 
def read_root():
    return {"Hello": "World"}


app.include_router(api_router, prefix="/api/v1")