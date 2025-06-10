from fastapi import APIRouter

router = APIRouter()

@router.get("/", summary="List all clients")
def list_clients():
    return [{"id": 1, "name": "ТОВ «Альфа»"}]
