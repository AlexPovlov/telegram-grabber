from sqlalchemy import Boolean, Column, Integer, String
from src.db.database import Base


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    phone = Column(String)
    phone_hash = Column(String, nullable=True)
    auth = Column(Boolean, default=False)
    state = Column(String, nullable=True)
