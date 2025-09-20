from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task_schema import TaskCreate, TaskPage, TaskOut
from fastapi import HTTPException
def create_task(db: Session, task: TaskCreate, owner_id: str):
    try:
        db_task = Task(
            title= task.title,
            description = task.description,
            owner_id = owner_id)
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return db_task
    except :
        raise HTTPException(status_code=400)

def get_tasks(db: Session, page: int = 1, limit: int = 10):
    # Tổng số task
    total_tasks = db.query(Task).count()
    skip = int((page-1)*limit)
    # Query phân trang
    data = (
        db.query(Task)
        .offset(skip)
        .limit(limit)
        .all()
    )

    # Tính toán phân trang
    current_page = (skip // limit) + 1 if limit > 0 else 1
    total_pages = (total_tasks + limit - 1) // limit if limit > 0 else 1

    return {
        "data": data,
        "current_page": current_page,
        "limit": limit,
        "skip": skip,
        "total": total_tasks,
        "total_pages": total_pages,
    }