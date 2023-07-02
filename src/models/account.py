from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from src.db.database import Base


class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    phone = Column(String, nullable=False)
    phone_hash = Column(String, nullable=True)
    auth = Column(Boolean, default=False, nullable=False)
    state = Column(String, nullable=True)
    # chats = relationship('Chat', back_populates="account")
