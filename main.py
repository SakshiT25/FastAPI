from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

@app.get("/")

# class user(BaseModel):
#     name: str
#     age: int
#     email: str
# def home():
#     return {"message":"Hello from vern"}

# @app.get("/about")
# def about():
#     return {"message":"This is a FastAPI application."}

# @app.get("/users/{user_id}")
# def users(user_id:int):
#     return {"user_id": user_id}

# @app.get("/users")
# def users(name: str=None):
#     return {"name": name}

# @app.get("/products")
# def products(limit:int=10):
#     return {"limit": limit} 

# @app.get("/items")
# def items(quantity:int=0, price:float=0.0):
#     return {"quantity":quantity, "price":price}

# @app.post("/create-user")
# def create_user(user: dict):
#     return {
#         "message": "data received successfully",
#         "data": user,
#         "status":"success"
#     }

# @app.post("/create-user2")
# def create_user2(user: user):
#     return {
#         "message": "data received successfully",
#         "data": user,
#         "status":"success"
#     }   

class Address(BaseModel):
    pincodeL: int
    city: str

class User(BaseModel):
    name: str
    age: int
    address: Address

@app.post("/create-user")
def create_user(user:User):
    return {
        "message": "data received successfully",
        "data": user, 
        "status":"success"
    }
    