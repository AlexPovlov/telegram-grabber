from tortoise.contrib.pydantic import pydantic_model_creator

from src.models.spam_chat import SpamChat

SpamChatSchema = pydantic_model_creator(
    SpamChat,
    exclude=(
        "chat",
        "account",
        "to_chats.account",
        "to_chats.account_id",
        "to_chats.grabber_chats",
        "to_chats.from_chat",
        "to_chats.spam_chat",
        "to_chats.spam_to_chats",
        "chat_id",
        "spam_chat"
    ),
)
