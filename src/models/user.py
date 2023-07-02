from sqlalchemy import Boolean, Column, Integer, String

from src.db.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String, nullable=True)
    password = Column(String)
    disabled = Column(Boolean, default=False)
