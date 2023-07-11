from tortoise.contrib.pydantic import pydantic_model_creator

from src.models.spam_chat import SpamChat

SpamChatSchema = pydantic_model_creator(
    SpamChat,
    exclude=("chat","account",),
)
