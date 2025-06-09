from fastapi import FastAPI
from src.api.v1 import api_router
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI(
    title="Symbios Legal Core API",
    version="0.1.0",
    openapi_url="/openapi.json",
)

@app.get("/.well-known/ai-plugin.json", include_in_schema=False)
def serve_manifest():
    return FileResponse(Path(__file__).parent / "gpt" / "manifest.json")

@app.get("/.well-known/openapi.yaml", include_in_schema=False)
def serve_openapi():
    return FileResponse(Path(__file__).parent / "gpt" / "openapi.yaml")

app.include_router(api_router, prefix="/api/v1")