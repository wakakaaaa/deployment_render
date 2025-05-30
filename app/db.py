from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings


DATABASE_URL = (
    f"redshift+redshift_connector://{settings.REDSHIFT_USER}:{settings.REDSHIFT_PASS}@"
    f"{settings.REDSHIFT_HOST}:{settings.REDSHIFT_PORT}/{settings.REDSHIFT_DB}"
)


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 依赖注入用
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()