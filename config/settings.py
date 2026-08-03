import os
from dotenv import load_dotenv

# for Loading environment variables from .env
load_dotenv()

BASE_URL = os.getenv("BASE_URL")
DATABASE_URL = os.getenv("DATABASE_URL")

if not BASE_URL:
    raise ValueError("BASE_URL is not set in the .env file")