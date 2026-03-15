from fastapi import FastAPI

app = FastAPI(title="YT FastAPI Project")

@app.get("/") 
def read_root():
    return {"Hello": "World"}
