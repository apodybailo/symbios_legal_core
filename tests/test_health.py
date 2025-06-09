from fastapi.testclient import TestClient
from src.api.v1.main import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
