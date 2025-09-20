from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
import uuid
from sqlalchemy.orm import relationship
from app.core.database import Base  

class Task(Base):
    __tablename__ = "tasks"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, index=True) # có thể thay  bằng UUID của postgre
    title = Column(String, nullable=False)
    description = Column(String)
    completed = Column(Boolean, default=False)
    owner_id = Column(String, ForeignKey("users.id"))

    owner = relationship("User", back_populates="tasks")