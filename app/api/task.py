from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.task_schema import TaskCreate, TaskOut, TaskPage
from app.services.task_service import create_task, get_tasks

router = APIRouter()

@router.post("/", response_model=TaskOut)
def create(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db, task, owner_id= task.user_id)  # giả sử owner_id là 1

#@router.get("/", response_model=TaskPage)
@router.get("/")
def read(page: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    return get_tasks(db, page, limit)