from fastapi import APIRouter, HTTPException
from . import schemas
from pydantic import BaseModel
from passlib.hash import pbkdf2_sha256
from typing import List
from .auth import (
    check_current_user,
    create_access_token,
    hash_password,
    verify_password,
)
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends

router = APIRouter()

Users = [
    {
        "name": "Dev",
        "email": "dev@mail.com",
        "password": "$2b$12$/qnUCogWEuVPx8AAV.hnle/r.dV7FHNSTEnchkh/sh1zwzh/XGqZa",
    },
    {
        "name": "Raj",
        "email": "raj@mail.com",
        "password": "$2b$12$/qnUCogWEuVPx8AAV.hnle/r.dV7FHNSTEnchkh/sh1zwzh/XGqZa",
    },
]


@router.get("/user", response_model=List[schemas.UserData])
def get_all_users():
    user_data = [schemas.UserCreate(**user) for user in Users]

    return user_data.model_dump(exclude="password")


# @router.post("/user")
# def create_user(user: schemas.UserCreate):
#     if any(u["email"] == user.email for u in Users):
#         raise HTTPException(status_code=404, detail="email repeated")

#     new_user = schemas.UserData(id=len(Users) + 1, name=user.name, email=user.email)
#     Users.append(dict(new_user))
#     return new_user


@router.post("/user")
def user_create(user: schemas.UserCreate):
    if any(u["email"] == user.email for u in Users):
        raise HTTPException(status_code=403, detail="email repeated")

    hashed_pasword = hash_password(user.password)

    new_user = {"name": user.name, "email": user.email, "password": hashed_pasword}
    Users.append(new_user)
    return schemas.UserData(name=user.name, email=user.email, )


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


@router.post("/login")
def login(data: schemas.UserLogin):

    user = next((u for u in Users if u["email"] == data.email))
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    if not verify_password(data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_access_token(data={"sub": user["email"], "name": user["name"]})
    return {"access_token": token}


@router.get("/me")
def get_me(current_user=Depends(check_current_user)):
    return {current_user["name"], current_user["email"]}
