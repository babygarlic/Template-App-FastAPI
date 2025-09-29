from sqlalchemy.orm import Session
from sqlalchemy import select, delete
from app.models.user import User
from app.models.task import Task
from app.schemas.user_schema import UserCreate, UserUpdate
from app.utils.security import get_password_hash
from fastapi import HTTPException

def checkUserIsExist(email: str, db: Session):
    isExist = db.query(User).filter(User.email == email).first()
    if (isExist): return True
    return False

def create_user(db: Session, user: UserCreate):

    exist_user =  checkUserIsExist(user.email,db)
    
    if(exist_user):
        raise HTTPException(status_code=400, detail="Email already exists")

    hashed_password = get_password_hash(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_all_users(page: int, limit: int ,db: Session):
    # Tổng số task
    total_users = db.query(User).count()
    skip = int((page-1)*limit)
    
    stmt = select(User.username, User.email, User.id, User.is_active, User.role).offset(skip).limit(limit)
    data = db.execute(stmt).mappings().all()

    current_page = (skip // limit) + 1 if limit > 0 else 1
    total_pages = (total_users + limit - 1) // limit if limit > 0 else 1

    return {
        "data":data,
        "current_page": current_page,
        "limit": limit,
        "skip": skip,
        "total_users": total_users,
        "total_pages": total_pages,
    }

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def delete_user(user_id: str, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    try:
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        query = delete(Task).where(Task.owner_id == user_id)
        db.execute(query)
        db.delete(user)
        db.commit()
        return {"message": "User deleted successfully"}
    finally:
        db.rollback()
        raise HTTPException(status_code=500, detail="An error occurred while deleting the user")
    
def acctivate_user(user_id: str,db: Session):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.is_active = not user.is_active
    db.commit()
    db.refresh(user)

    return user
