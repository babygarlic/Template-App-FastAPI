from sqlalchemy import Column, Integer, String,TIMESTAMP

from sqlalchemy.orm import relationship
import uuid
from app.core.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, default="user")
    is_active = Column(Integer, default=0)  # 1: active, 0: inactive
    otp_code = Column(String, index=True, nullable=True) 
    otp_created_at = Column(TIMESTAMP, nullable=True)
    otp_expiration = Column(TIMESTAMP, nullable=True) # có thể xử lý bằng trigger trong postgre

    tasks = relationship("Task", back_populates="owner")