import os
from pydantic_settings import BaseSettings,SettingsConfigDict
from dotenv import load_dotenv
import os

load_dotenv()
class Settings(BaseSettings):
    # REDSHIFT_USER: str
    # REDSHIFT_PASS: str
    # REDSHIFT_HOST: str
    # REDSHIFT_PORT: int = 5439
    # REDSHIFT_DB: str
    mysql_user: str = os.getenv("mysql_user")
    mysql_pass: str = os.getenv("mysql_pass")
    mysql_host: str = os.getenv("mysql_host")
    mysql_port: int = 3306
    mysql_db: str = os.getenv("mysql_db")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()