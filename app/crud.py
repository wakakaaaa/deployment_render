from sqlalchemy.orm import Session
from sqlalchemy import text

def fetch_data(db: Session, query: str):
    result = db.execute(text(query))
    return result.fetchall()