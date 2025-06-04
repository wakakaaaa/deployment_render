from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import get_settings
import os
import pymysql
pymysql.install_as_MySQLdb()

# DATABASE_URL = (
#     f"redshift+redshift_connector://{settings.REDSHIFT_USER}:{settings.REDSHIFT_PASS}@"
#     f"{settings.REDSHIFT_HOST}:{settings.REDSHIFT_PORT}/{settings.REDSHIFT_DB}"
# )
# engine = create_engine(DATABASE_URL)

mysql_url = (
    f"mysql+pymysql://{get_settings.MYSQL_USER}:{get_settings.MYSQL_PASS}@{get_settings.MYSQL_HOST}:{get_settings.MYSQL_PORT}/"
    f"{get_settings.MYSQL_DB}"
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