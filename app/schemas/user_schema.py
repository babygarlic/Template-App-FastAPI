from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    password: str | None = None

class UserOut(UserBase):
    id: str

class Config: # config cho phép Pydantic đọc dữ liệu từ SQLAlchemy model — tức là từ các đối tượng ORM.
    from_attributes = True

# v0.1.1 sẽ thêm tính năng RequestValidationError