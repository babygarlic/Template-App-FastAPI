from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.config import settings    
from app.core.database import get_db
from app.schemas.user_schema import UserCreate, UserOut, UserUpdate
from app.utils.security import create_token, verify_password
from app.services.mail_service import send_activation_email
from datetime import datetime, timedelta
from app.utils.security import create_otp_code
from app.services.user_service import (
    create_user,
    get_user,
    get_user_by_email
    )

router = APIRouter()

@router.post("/register", response_model=UserOut)
async def create(user: UserCreate, db: Session = Depends(get_db)):
    """Đăng ký user mới"""
    user = create_user(db, user)
    if not user:
        raise HTTPException(status_code=400, detail="User creation failed")
    
    return user

@router.get("/me", response_model=UserOut)
def read_current_user(user_id: str, db: Session = Depends(get_db)):
    """Lấy thông tin user hiện tại"""
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/login", response_model=UserOut)
def login(email: str, password: str, db: Session = Depends(get_db)):
    """Đăng nhập user"""
    user = get_user_by_email(db=db, email=email)

    if not user or not verify_password(password):
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    expires_delta= settings.EXPRIES_DELTA
    token_type= settings.TOKEN_TYPE
    token_data = {
        "user_id": user.id,
        "email": user.email,
        "role": user.role
    }

    token = create_token(token_data, expires_delta )
    return {
        "access_token": token,
        "token_type": token_type,
        "expires_in": expires_delta,
        }  

@router.get("/otp{email}", response_model=UserOut)
def send_otp(email: str, db: Session = Depends(get_db)):
    """Gửi mã OTP đến email"""
    user = get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    otp_code = create_otp_code()
    # Lưu mã OTP vào cơ sở dữ liệu hoặc bộ nhớ tạm thời
    user.otp_code = otp_code
    user.otp_expiration = datetime.utcnow() + timedelta(minutes=10)  # Mã OTP hợp lệ trong 10 phút
    db.commit()
    db.refresh(user)

    # Gửi email chứa mã OTP
    send_activation_email(email, otp_code)

    return {"message": "OTP code sent to your email"}

@router.post("/activate", response_model=UserOut)
def activate_user(email: str, db: Session = Depends(get_db)):
    """Kích hoạt user"""
    user = get_user(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user.is_active:
        raise HTTPException(status_code=400, detail="User already activated")
    
    user.is_active = 1
    db.commit()
    db.refresh(user)
    return user

@router.post("/logout", response_model=dict)
def logout():
    """Đăng xuất user"""
    pass

@router.post("/change-password", response_model=dict)
def change_password():
    """Đổi mật khẩu"""
    pass

