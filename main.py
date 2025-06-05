from fastapi import FastAPI
from app.api import auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(auth.router, prefix="/auth")
# ✅ Cho phép frontend kết nối
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # domain Next.js
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
