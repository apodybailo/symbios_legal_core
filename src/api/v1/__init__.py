from fastapi import APIRouter
from .main      import router as main_router
from .clients   import router as clients_router
from .companies import router as companies_router
from .generate  import router as generate_router
from .email     import router as email_router

api_router = APIRouter()

# **Обов’язково** підключаємо health із пустим prefix
api_router.include_router(main_router,       prefix="",          tags=["meta"])
api_router.include_router(clients_router,   prefix="/clients",  tags=["clients"])
api_router.include_router(companies_router, prefix="/companies",tags=["companies"])
api_router.include_router(generate_router,  prefix="/generate", tags=["generate"])
api_router.include_router(email_router,     prefix="/email",    tags=["email"])