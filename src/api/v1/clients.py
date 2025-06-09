from fastapi import APIRouter, Depends
from ..deps import get_db
router = APIRouter()

@router.get("/health", summary="Healthcheck", include_in_schema=False)
async def health():
    return {"status": "ok", "router": "clients"}
