from app.models.Users import User
from fastapi import APIRouter, HTTPException, Depends
from app.schemas.UserSchema import UserCreate, UserLogin
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from app.dependency.auth import get_db, create_access_token
from app.crud.user import create_user, get_user_by_email, login_user, get_all_users
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
    return {"user": created_user}


@router.post("/login")
async def login(user: UserLogin, db: AsyncSession = Depends(get_db)):
    authenticated_user = await login_user(db, user)
    if not authenticated_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token_data = {
        "user_id": authenticated_user.id,
        "email": authenticated_user.email,
        "name": authenticated_user.name
    }
    access_token = create_access_token(data=token_data)
    
    return {
        "access_token": access_token
    }


@router.get("/users")
async def list_users(db: AsyncSession = Depends(get_db)):
    users = await get_all_users(db)
    users_list = []
    for user in users:
        user_dict = {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
        users_list.append(user_dict)
    return {"users": users_list}
