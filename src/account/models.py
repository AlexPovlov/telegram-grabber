from sqlalchemy import String, Column, Integer, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    phone = Column(String)
    phone_hash = Column(String, nullable=True)
    auth = Column(Boolean, default=False)
    state = Column(String, nullable=True)

def account():
    return Account