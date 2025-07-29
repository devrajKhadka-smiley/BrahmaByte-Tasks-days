from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    model_config ={
        "extra": "forbid"
    }

class UserData(BaseModel):
    name: str
    email: str
    password: str
    model_config ={
        "extra": "forbid"
    }


class UserUpdate(BaseModel):
    name: str | None = None
    email: str | None
    model_config ={
        "extra": "forbid"
    }

class UserLogin(BaseModel):
    email: str
    password: str
    model_config = {
        "extra": "forbid"
    }
    