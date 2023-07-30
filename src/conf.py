from os import getenv

from dotenv import load_dotenv

load_dotenv()

APP_NAME=getenv("APP_NAME")
APP_DEBUG=getenv("APP_DEBUG")
APP_URL=getenv("APP_URL")
ORIGIN_DOMAINS=getenv("ORIGIN_DOMAINS").split(',')

DB_HOST=getenv("DB_HOST")
DB_USER=getenv("DB_USER")
DB_PASSWORD=getenv("DB_PASSWORD")
DB_NAME=getenv("DB_NAME")

SECRET_KEY = getenv("SECRET_KEY")
ALGORITHM = getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

TELEGRAM_API_ID = getenv("TELEGRAM_API_ID")
TELEGRAM_API_HASH = getenv("TELEGRAM_API_HASH")
TELEGRAM_APP_VERSION = getenv("TELEGRAM_APP_VERSION")
TELEGRAM_DEVICE = getenv("TELEGRAM_DEVICE")

path_errors = "logs/errors.log"

models = [
    "src.models.account",
    "src.models.chat",
    "src.models.grabber_chat",
    "src.models.spam_chat",
    "src.models.user",
    "src.models.spam_filter",
]
