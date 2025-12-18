from fastapi import APIRouter, Depends
from core.database import get_db
from sqlalchemy.orm import Session
from models.users import User
from dtos.users import UserRes
from utils.apiResponse import APIResponse
from typing import List

userRoutes = APIRouter(tags=["Users"])

@userRoutes.get("/", response_model=List[UserRes])
def get_all_users(db: Session = Depends(get_db)):
    try:
        db_users = db.query(User).all()
        return db_users
    except Exception as e:
        print("Error retrieving users:", e)
        return APIResponse.generateError(status_code=400, message="Failed to retrieve users")

@userRoutes.get("/{user_id}", response_model=UserRes)
def get_user_by_id(user_id: str, db: Session = Depends(get_db)):
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if user is None:
            return APIResponse.generateError(status_code=404, message="User not found")
        return user
    except Exception as e:
        print("Error retrieving user:", e)
        return APIResponse.generateError(status_code=400, message="Failed to retrieve user")