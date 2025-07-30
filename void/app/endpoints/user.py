from app.models.Users import User
from fastapi import APIRouter, HTTPException, Depends
from app.schemas.UserSchema import UserCreate, UserLogin
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from app.dependency.auth import get_db
from app.crud.user import create_user, get_user_by_email, login_user
from sqlalchemy import select


router = APIRouter()


@router.post("/signup")
async def signup(user: UserCreate, db: AsyncSession = Depends(get_db)):
    existing_email = await get_user_by_email(db, user.email)
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already registered")

    result = await db.execute(select(User).where(User.name == user.name))
    existing_name = result.scalars().first()
    if existing_name:
        raise HTTPException(status_code=400, detail="Name already registered")

    created_user = await create_user(db, user)
    return {"message": "User created", "user": created_user}


@router.post("/login")
async def login(user: UserLogin, db: AsyncSession = Depends(get_db)):
    authenticated_user = await login_user(db, user)
    if not authenticated_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful", "user_id": authenticated_user.id}


# @router.get("/users", response_model=list[User])
# async def list_users(user: UserLogin):
#     pass
