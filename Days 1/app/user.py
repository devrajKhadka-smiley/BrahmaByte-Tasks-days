from fastapi import APIRouter, HTTPException
from . import schemas
from pydantic import BaseModel
from typing import List

router = APIRouter()

Users = [
    {"id": 1, "name": "Dev", "email": "dev@mail.com"},
    {"id": 2, "name": "Raj", "email": "Raj@mail.com"},
    {"id": 3, "name": "Shyam", "email": "shyam@mail.com"},
    {"id": 4, "name": "Hari", "email": "hari@mail.com"},
    {"id": 5, "name": "Krishna", "email": "krishna@mail.com"},
]

class something(BaseModel):
    name: str = "success"
    
@router.get("/user",response_model=List[something])
def get_all_users():
    user_data = [schemas.UserData(**user) for user in Users]
    return user_data


@router.post("/user")
def create_user(user: schemas.UserCreate):
    if any(u["email"] == user.email for u in Users):
        raise HTTPException(status_code=404, detail="email repeated")

    new_user = schemas.UserData(id=len(Users) + 1, name=user.name, email=user.email)
    Users.append(dict(new_user))
    return new_user


@router.put("/user/{user_name}")
def put_user(user_name: str, user: schemas.UserCreate):
    for u in Users:
        if u["name"] == user_name:
            u["name"] = user.name
            u["email"] = user.email
            return schemas.UserData(**u)
    raise HTTPException(status_code=404, detail="User not found")


@router.patch("/user/{user_name}")
def patch_user(user_name: str, user: schemas.UserUpdate):
    for u in Users:
        if u["name"] == user_name:
            if user.name:
                u["name"] = user.name
            if user.email:
                u["email"] = user.email
            return schemas.UserUpdate(**u)
    raise HTTPException(status_code=404, detail="User not found")
