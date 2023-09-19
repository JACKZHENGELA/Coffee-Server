from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello":"World!"}

@app.get("/about")
def read_root():
    return {"Name":"Jack Zheng!"}