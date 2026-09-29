from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
def test_home(): assert client.get("/").status_code==200
def test_docs(): assert client.get("/docs").status_code==200
