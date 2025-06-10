from fastapi import FastAPI
from app.api_routes import router

app = FastAPI(title="GloRA: Global Retrieval Agent")
app.include_router(router)