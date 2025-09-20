from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Load biến môi trường từ file .env
load_dotenv()

# Lấy URL kết nối từ biến môi trường
DATABASE_URL = os.getenv("DATABASE_URL")

# Tạo engine
engine = create_engine(DATABASE_URL)

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