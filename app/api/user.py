from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.user_schema import UserCreate, UserOut, UserUpdate
from app.services.user_service import (
    create_user, 
    get_user, 
    get_user, 
    delete_user,
    get_all_users
)
router = APIRouter()

@router.post("/", response_model=UserOut)
async def create(user: UserCreate, db: Session = Depends(get_db)):
    """Tạo user mới"""
    return create_user(db, user)

@router.get("/")
def read_users(page:int =1,limit: int =10, Session = Depends(get_db)):
    """Danh sách các user"""
    users = get_all_users(+page, +limit,Session)
    return users

@router.get("/{user_id}", response_model=UserOut)
def read(user_id: str, db: Session = Depends(get_db)):
    """Lấy thông tin user theo ID"""
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}")
async def delete(user_id: str,db: Session= Depends(get_db)):
    """Xóa user theo ID"""
    status_del = delete_user(user_id, db)
    return status_del

@router.patch("/{user_id}")
async def update(user_id: str,user_update: UserUpdate, db: Session= Depends(get_db)):
    """Cập nhật user theo ID"""
    #user = update_user(user_id,user_update, db)
    #return user 
    pass