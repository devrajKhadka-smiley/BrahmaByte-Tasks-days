from passlib.context import CryptContext
from datetime import timedelta
from datetime import datetime, timedelta
from fastapi import Request, HTTPException
from jose import JWTError, jwt
from passlib.hash import pbkdf2_sha256
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


def check_current_user(request: Request):
    from .user import Users

    token = request.headers.get("Authorization")
    print(token)

    if token.startswith("Bearer "):
        token = token[len("Bearer ") :]
    else:
        raise HTTPException(status_code=401, detail="Invalid token header format")

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print(payload)
        email = payload.get("sub")
        print(email)

        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        user = next((u for u in Users if u["email"] == email))
        
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")

        return user

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token hi")
