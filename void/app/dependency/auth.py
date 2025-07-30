from passlib.context import CryptContext
from jose import jwt
from app.db.database import AsyncSessionLocal

# from .user import Users


SECRET_KEY = "0hUqz6XB1lBRZTDMNvmnIBj8Vc40WSgc"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 5


# pwd_context xai is an object that knows how to hash and verify with future proof depreciation
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(
    data: dict,
):
    to_encode = data.copy()
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
