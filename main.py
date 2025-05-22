from app import app
import uvicorn
from app.db.base import Base, engine
from app.db import models

#Criação de Tabelas
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)