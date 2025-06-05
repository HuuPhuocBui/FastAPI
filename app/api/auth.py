from fastapi import APIRouter, HTTPException
from app.schemas.user import UserCreate, UserLogin
from app.services.auth_service import register_user, authenticate_user

router = APIRouter()

@router.post("/register", tags=["Auth"])
async def register(user: UserCreate):
    result = await register_user(user)
    if not result:
        raise HTTPException(status_code=400, detail="Username already exists")
    return {"msg": "User registered successfully"}

@router.post("/login", tags=["Auth"])
async def login(user: UserLogin):
    token = await authenticate_user(user)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return {"access_token": token, "token_type": "bearer"}
