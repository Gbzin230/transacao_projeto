from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from .base import Base

class Transacao(Base):
    __tablename__ = "transacoes"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, nullable=False)
    valor = Column(Float, nullable=False)
    tipo = Column(String, nullable=False)
    data = Column(DateTime, default=datetime.utcnow)

