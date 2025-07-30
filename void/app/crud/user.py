from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from app.models.Users import User
from app.schemas.UserSchema import UserCreate, UserLogin
from app.dependency.auth import hash_password, verify_password
from sqlalchemy.inspection import inspect
from sqlalchemy import select

def to_dict(obj):
    return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}

async def create_user(db: AsyncSession, user: UserCreate):
    hashed_pw = hash_password(user.password)
    db_user = User(name=user.name, email=user.email, hashed_password=hashed_pw)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)  

    user_dict = to_dict(db_user)
    user_dict.pop("hashed_password", None)
    return user_dict


async def login_user(db: AsyncSession, user: UserLogin):
    db_user = await get_user_by_email(db, user.email)
    if not db_user:
        return None
    if not verify_password(user.password, db_user.hashed_password):
        return None
    return db_user


async def get_all_users(db: AsyncSession):
    result = await db.execute(select(User))
    return result.scalars().all()

async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(User).where(User.email == email))
    return result.scalars().first()

