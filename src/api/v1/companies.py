from fastapi import APIRouter, HTTPException
from src.adapters.opendatabot import get_company

router = APIRouter()

@router.get("/{edrpou}", summary="Get company info")
def get_company_info(edrpou: str):
    data = get_company(edrpou)
    if not data:
        raise HTTPException(404, "Not found")
    return data