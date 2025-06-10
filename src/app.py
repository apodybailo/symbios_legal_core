# src/app.py
from fastapi import FastAPI
from src.api.v1 import api_router

app = FastAPI(
    title="Symbios Legal Core API",
    version="0.1.0",
    openapi_url="/.well-known/openapi.json",
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/", include_in_schema=False)
async def root():
    return {"message": "Legal Core is up"}