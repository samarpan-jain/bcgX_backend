from fastapi import APIRouter, Depends, HTTPException
from core.database import get_db
from utils.encryptPass import hash_password, verify_password
from utils.apiResponse import APIResponse
from dtos.users import UserDTO
from models.users import User
from sqlalchemy.orm import Session

authRoutes = APIRouter(tags=["Authentication"])

@authRoutes.get("/login/{email}/{password}", status_code=200)
def login(email: str, password: str, db: Session = Depends(get_db)):
    try:
        user = db.query(User).filter(User.email == email).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        if verify_password(password, user.password) is False:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return APIResponse.generateSuccess(status_code=200,message="Login successful")
    except Exception as e:
        print("Error during login:", e)
        raise HTTPException(status_code=400, detail="Login failed")

@authRoutes.post("/register", status_code=200)
def register(userDTO: UserDTO, db: Session = Depends(get_db)):
    try:
        if(db.query(User).filter(User.email == userDTO.email).first()):
            return APIResponse.generateError(status_code=400, message="Email already registered")
        userDTO.password = str(hash_password(userDTO.password))
        user=User(**userDTO.model_dump())
        db.add(user)
        db.commit()
        return APIResponse.generateSuccess(status_code=200,message="User registered successfully")
    except Exception as e:
        print("Error registering user:", e)
        return APIResponse.generateError(status_code=400, message="Registration failed")