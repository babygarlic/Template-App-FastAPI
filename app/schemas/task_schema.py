from pydantic import BaseModel, Field, validator

class TaskBase(BaseModel):
    title: str
    description: str | None = None

class TaskCreate(TaskBase):
    user_id: str

class TaskOut(TaskBase):
    id: str
    completed: bool
    owner_id: str

class TaskPage(BaseModel):
    data: list[TaskOut]
    current_page: int
    limit: int
    skip: int
    total: int
    total_pages:int

class Config:
    from_attributes = True
