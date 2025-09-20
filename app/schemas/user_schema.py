from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: str

    class Config: # config cho phép Pydantic đọc dữ liệu từ SQLAlchemy model — tức là từ các đối tượng ORM.
        from_attributes = True 
