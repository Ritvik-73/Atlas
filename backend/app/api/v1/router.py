from fastapi import APIRouter

router = APIRouter(prefix="/api/v1")

@router.get("/health", tags=["health"])
def health_check_v1():
    return {"status": "ok", "version":"v1"}

