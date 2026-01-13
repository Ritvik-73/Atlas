from fastapi import APIRouter
from app.api.v1.users import router as users_router

router = APIRouter(prefix="/api/v1")

@router.get("/health", tags=["health"])
def health_check_v1():
    return {"status": "ok", "version":"v1"}


router.include_router(users_router)
