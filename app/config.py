import os
from pydantic_settings import BaseSettings,SettingsConfigDict
from dotenv import load_dotenv
import os

load_dotenv()
class Settings(BaseSettings):
    REDSHIFT_USER: str
    REDSHIFT_PASS: str
    REDSHIFT_HOST: str
    REDSHIFT_PORT: int = 5439
    REDSHIFT_DB: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()