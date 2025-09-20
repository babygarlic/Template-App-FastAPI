from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings


# Tạo engine
engine = create_engine(settings.DATABASE_URL)

# Tạo session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Tạo base class cho các model
Base = declarative_base()

# Lấy kết nối với database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()