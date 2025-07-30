from sqlalchemy import Column, Integer, String
from app.db.database import Base



class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
    )
    name = Column(
        String,
        unique=True,
    )
    email = Column(String, unique=True)
    hashed_password = Column(String, nullable=False)
