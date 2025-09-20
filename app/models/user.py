from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import uuid
from app.core.database import Base  # hoặc nơi bạn khai báo Base

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)

    tasks = relationship("Task", back_populates="owner")