from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()
BASE_DIR = Path(__file__).parent.parent


class BaseSetting(BaseSettings):
    class Config:
        env_file_encoding = "UTF-8"
        extra = "allow"
