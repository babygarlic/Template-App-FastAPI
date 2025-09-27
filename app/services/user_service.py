from sqlalchemy.orm import Session
from app.models.user import User
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
    # Query phân trang
    data = (
        db.query(User)
        .offset(skip)
        .limit(limit)
        .all()
    )

    # Tính toán phân trang
    current_page = (skip // limit) + 1 if limit > 0 else 1
    total_pages = (total_users + limit - 1) // limit if limit > 0 else 1

    return {
        "data": data,
        "current_page": current_page,
        "limit": limit,
        "skip": skip,
        "total_users": total_users,
        "total_pages": total_pages,
    }


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def delete_user(user_id: str, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}
async def update_user(user_id: str,user_update: UserUpdate ,db: Session):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.is_active = not user.is_active
    db.commit()
    db.refresh(user)
    return user