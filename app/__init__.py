from fastapi import FastAPI
from .api import router as api_router

app = FastAPI(title = "API de Transações")

#Inclui rotas do blueprint
app.include_router(api_router, prefix="/api")