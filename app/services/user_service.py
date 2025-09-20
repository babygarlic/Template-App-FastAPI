from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user_schema import UserCreate
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

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()