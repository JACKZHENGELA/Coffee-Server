from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello":"World!"}


@app.get("/about")
def read_about():
    return {"Name":"Jack Zheng!"}


@app.get("/user/{user_id}")
def read_user(user_id: str):
    return{"id": user_id}

if __name__ == "__main__":
    uvicorn.run("main:app",reload=True)