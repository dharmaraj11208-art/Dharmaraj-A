from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .database import init_db
from .routes import router
BASE_DIR=Path(__file__).resolve().parent.parent
app=FastAPI(title="FitBuddy – AI Fitness Plan Generator",version="1.0.0")
app.mount("/static",StaticFiles(directory=str(BASE_DIR/"static")),name="static")
@app.on_event("startup")
def startup(): init_db()
app.include_router(router)
