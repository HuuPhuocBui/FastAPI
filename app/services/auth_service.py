from passlib.context import CryptContext
from app.core.database import db
from app.core.jwt import create_access_token
from app.schemas.user import UserCreate, UserLogin

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def register_user(user: UserCreate):
    if await db.users.find_one({"username": user.username}):
        return None
    hashed_pw = pwd_context.hash(user.password)
    await db.users.insert_one({
        "username": user.username,
        "email": user.email,
        "hashed_password": hashed_pw
    })
    return {"msg": "User created successfully"}

async def authenticate_user(user: UserLogin):
    db_user = await db.users.find_one({"username": user.username})
    if not db_user:
        return None
    if not pwd_context.verify(user.password, db_user["hashed_password"]):
        return None
    return create_access_token({"sub": user.username})
