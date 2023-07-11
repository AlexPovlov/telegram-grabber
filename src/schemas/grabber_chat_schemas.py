from tortoise.contrib.pydantic import pydantic_model_creator

from src.models.grabber_chat import GrabberChat

GrabberChatSchema = pydantic_model_creator(
    GrabberChat,
    exclude=(
        "from_chat.account",
        "from_chat.spam_chats",
        "chat",
    ),
)
