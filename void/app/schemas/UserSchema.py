from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    model_config = {"extra": "forbid"}


class UserLogin(BaseModel):
    email: str
    password: str
    model_config = {"extra": "forbid"}
    
