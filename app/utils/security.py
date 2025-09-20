from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# mã hóa mật khẩu
def get_password_hash(password: str):
    return pwd_context.hash(password)