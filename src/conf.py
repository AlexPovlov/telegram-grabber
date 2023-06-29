from os import getenv

from dotenv import load_dotenv

load_dotenv()

DB_CONNECTION_URI = getenv("DB_CONNECTION_URI")

SECRET_KEY = getenv("SECRET_KEY")
ALGORITHM = getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

TELEGRAM_API_ID = getenv("TELEGRAM_API_ID")
TELEGRAM_API_HASH = getenv("TELEGRAM_API_HASH")
TELEGRAM_APP_VERSION = getenv("TELEGRAM_APP_VERSION")
TELEGRAM_DEVICE = getenv("TELEGRAM_DEVICE")

path_errors = "logs/errors.log"
