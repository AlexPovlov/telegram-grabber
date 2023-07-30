from .services.spam_chat_service import SpamChatService
from .repositories.spam_chat_repository import SpamChatRepository
from .models.spam_chat import SpamChat

from .services.spam_filter_service import SpamFilterService
from .repositories.spam_filter_repository import SpamFilterRepository
from .models.spam_filter import SpamFilter

from .services.account_service import AccountService
from .repositories.account_repository import AccountRepository
from .models.account import Account

def spam_service():
    return SpamChatService(SpamChatRepository(SpamChat))

def filter_service():
    return SpamFilterService(SpamFilterRepository(SpamFilter))

def account_service():
    return AccountService(AccountRepository(Account))