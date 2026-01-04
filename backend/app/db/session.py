from sqlalchemy.orm import sessionmaker
from backend.app.db.engine import engine

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)
