import os

from dotenv import load_dotenv

load_dotenv()

# fast-api settings
API_PORT = int(os.environ.get("API_PORT"))
API_HOST = os.environ.get("API_HOST")
API_RELOAD = bool(os.environ.get("API_RELOAD"))

# database
DATABASE_URL = os.environ.get("DATABASE_URL")