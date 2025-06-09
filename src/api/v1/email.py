from fastapi import APIRouter
router = APIRouter()

@router.get("/health", summary="Healthcheck", include_in_schema=False)
async def health():
    return {"status": "ok", "router": "email"}
