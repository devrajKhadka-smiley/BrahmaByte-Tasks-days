from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    model_config ={
        "extra": "forbid"
    }


class UserData(BaseModel):
    id: int
    name: str
    email: str


class UserUpdate(BaseModel):
    name: str | None = None
    email: str | None
