from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import get_settings
import os
import pymysql
pymysql.install_as_MySQLdb()
settings = get_settings()

# DATABASE_URL = (
#     f"redshift+redshift_connector://{settings.REDSHIFT_USER}:{settings.REDSHIFT_PASS}@"
#     f"{settings.REDSHIFT_HOST}:{settings.REDSHIFT_PORT}/{settings.REDSHIFT_DB}"
# )
# engine = create_engine(DATABASE_URL)

mysql_url = (
    f"mysql+pymysql://{settings.MYSQL_USER}:{settings.MYSQL_PASS}@{settings.MYSQL_HOST}:{settings.MYSQL_PORT}/"
    f"{settings.MYSQL_DB}"
)
# mysql_url = (
#     f"mysql://root:TkRZtpXAQfVrnVvGZASsLQAmxdGKGoZC@centerbeam.proxy.rlwy.net:41908/railway"
# )
engine = create_engine(mysql_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 依赖注入用
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()