from fastapi import FastAPI

import uvicorn


app = FastAPI()

users = [
    {"name": "Jack", "grade": 10},
    {"name": "Hudson", "grade": 11},
    {"name": "Nolan", "grade": 10},
]

@app.get("/users/me")
async def get_me():
    return {"Me": "Jack"}

@app.get("/users/{user_id}")
async def get_profile(user_id: int):
    if user_id < 0 or user_id > len(users) - 1:
        return {"message": "User not found"}
    user = users[user_id]
    return {"data": user}

@app.get("/documents")
async def get_document(name: str, age: int):
    if name and age:
        return {"name": name, "age": age}
    return {"msg": "Got docs successfully"}

@app.get("/secret")
async def get_secret():
    return "Chemistry is shit."


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)
