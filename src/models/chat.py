from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.db.database import Base


class Chat(Base):
    __tablename__ = "chats"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    chat_id = Column(String, nullable=False, unique=True)
    account_id = Column(Integer, ForeignKey("accounts.id", ondelete="CASCADE"))


class ChatToChat(Base):
    __tablename__ = "chat_to_chat"
    id = Column(Integer, primary_key=True)
    from_chat_id = Column(Integer, ForeignKey(Chat.id, ondelete="CASCADE"))
    to_chat_id = Column(Integer, ForeignKey(Chat.id, ondelete="CASCADE"))
    last_message = Column(String, nullable=True)
