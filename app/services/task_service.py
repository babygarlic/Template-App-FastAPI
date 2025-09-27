from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession ## cân nhắc nên dùng bất đồng bộ cho hệ thống lớn
from app.models.task import Task
from app.schemas.task_schema import TaskCreate, TaskPage, TaskOut
from fastapi import HTTPException
def create_task(db: Session, task: TaskCreate, owner_id: str): # Tạo task
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

def get_tasks(db: Session, page: int = 1, limit: int = 10): #Lấy danh sách task với phân trang
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
        "total_tasks": total_tasks,
        "total_pages": total_pages,
    }

def complete_task(db: Session, task_id: str): # Đánh dấu hoàn thành
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        task.completed = True
        db.commit()
        db.refresh(task)
    return task

def delete_task(task_id: str, db: Session): # Xóa task
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
        return {"message": "Task deleted successfully"}
    return {"message": "Task not found"}

def update_task(task_id: int, task_update: TaskCreate, db: Session): # Cập nhật task
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        task.title = task_update.title
        task.description = task_update.description
        db.commit()
        db.refresh(task)
    return task

def get_task_complete(db: Session, page: int = 1, limit: int = 10): #Lấy danh sách task đã hoàn thành với phân trang
    # Tổng số task
    total_tasks = db.query(Task).count()
    # Tổng số task đã hoàn thành
    total_tasks_complete = db.query(Task).filter(Task.completed == True).count()
    # Tổng số task chưa hoàn thành
    total_tasks_incomplete = total_tasks - total_tasks_complete

    skip = int((page-1)*limit)
    # Query phân trang
    data = (
        db.query(Task)
        .filter(Task.completed == True)
        .offset(skip)
        .limit(limit)
        .all()
    )

    # Tính toán phân trang
    current_page = (skip // limit) + 1 if limit > 0 else 1
    total_pages = (total_tasks + limit - 1) // limit if limit > 0 else 1

    return {
        "data": data,
        "total": total_tasks,"total": total_tasks,
        "task_complete": total_tasks_complete,
        "task_incomplete": total_tasks_incomplete,
        "current_page": current_page,
        "limit": limit,
        "skip": skip,
        "total_pages": total_pages,
    }