from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.user_schema import UserCreate, UserOut
from app.services.user_service import create_user, get_user

router = APIRouter()

@router.post("/", response_model=UserOut)
async def create(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)


@router.get("/{user_id}", response_model=UserOut)
def read(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
