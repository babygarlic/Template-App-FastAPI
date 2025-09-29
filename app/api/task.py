from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.task_schema import TaskCreate, TaskOut
from app.services.task_service import (
    create_task,
    get_tasks ,
    complete_task, 
    delete_task, 
    update_task, 
    get_task_complete
)

router = APIRouter()

@router.post("/", response_model=TaskOut)
async def create(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db, task, owner_id= task.user_id)

@router.get("/")
async def read(page: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    """Lấy danh sách task với phân trang"""
    return get_tasks(db, page, limit)

@router.get("/complete")
async def read_task_complete(db: Session = Depends(get_db)):
    """Lấy danh sách task đã hoàn thành"""
    task = get_task_complete(db)
    return task

@router.patch("/{task_id}/complete", response_model=TaskOut)
async def complete(task_id: str, db: Session = Depends(get_db)):
    """Đánh dấu task là hoàn thành"""
    task = complete_task(db, task_id)
    return task

@router.delete("/{task_id}", response_model=dict)
async def delete(task_id: str, db: Session = Depends(get_db)):
    """Xóa task"""
    task = delete_task(task_id, db)
    return task

@router.patch("/{task_id}", response_model=TaskOut)
async def update(task_id: int, task_update: TaskCreate, db: Session = Depends(get_db)):
    """Cập nhật thông tin task"""
    task = update_task(task_id, task_update, db)
    return task
