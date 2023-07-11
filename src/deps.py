from .services.spam_chat_service import SpamChatService
from .repositories.spam_chat_repository import SpamChatRepository
from .models.spam_chat import SpamChat


def spam_service():
    return SpamChatService(SpamChatRepository(SpamChat))
