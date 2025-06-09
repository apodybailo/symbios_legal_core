from fastapi import APIRouter
from . import main as main_router, templates, clients, cases, generate, email, cicd

api_router = APIRouter()
api_router.include_router(main_router.router, tags=["meta"])
api_router.include_router(templates.router, prefix="/templates", tags=["templates"])
api_router.include_router(clients.router, prefix="/clients", tags=["clients"])
api_router.include_router(cases.router, prefix="/cases", tags=["cases"])
api_router.include_router(generate.router, prefix="/generate", tags=["generate"])
api_router.include_router(email.router, prefix="/email", tags=["email"])
api_router.include_router(cicd.router, prefix="/cicd", tags=["cicd"])
