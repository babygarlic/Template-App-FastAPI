from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
from app.core.config import settings
import random

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str)-> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_otp_code()-> str:
    return str(random.randint(100000, 999999))

def verify_otp_code(otp_code: str, user_email: str)->bool:
    # Xác thực mã OTP (ví dụ: kiểm tra trong cơ sở dữ liệu)
    # Giả sử bạn có một hàm get_user_by_email để lấy thông tin người dùng từ cơ sở dữ liệu
    # user = get_user_by_id(user_id)
    # if user and user.otp_code == otp_code and user.otp_expiration > datetime.utcnow():
    #     return True
    # return False
    pass    

def create_token(data: dict, expires_delta: int)-> str:
    secret_key = settings.SECRET_KEY
    algorithm = settings.ALGORITHM

    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(seconds=expires_delta)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm)

    return encoded_jwt

def decode_token(token: str):
    secret_key = settings.SECRET_KEY
    algorithm = settings.ALGORITHM
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        return payload
    except JWTError:
        return None
    