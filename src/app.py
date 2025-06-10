# src/app.py
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path
from src.api.v1 import api_router

BASE = Path(__file__).parent

app = FastAPI(
    title="Symbios Legal Core API",
    version="0.1.0",
    openapi_url="/.well-known/openapi.json",  # (опційно)
)

# 1) Роздача OpenAPI-YAML
@app.get("/.well-known/openapi.yaml", include_in_schema=False)
def serve_openapi():
    path = BASE / "gpt" / "openapi.yaml"
    return FileResponse(path, media_type="text/yaml")

# 2) (Опціонально) Роздача manifest для ChatGPT Plugin
@app.get("/.well-known/ai-plugin.json", include_in_schema=False)
def serve_manifest():
    path = BASE / "gpt" / "manifest.json"
    return FileResponse(path, media_type="application/json")

# 3) Включаємо всі API-роути
app.include_router(api_router, prefix="/api/v1")

# 4) Кореневий простий endpoint
@app.get("/", include_in_schema=False)
async def root():
    return {"message": "Legal Core is up"}