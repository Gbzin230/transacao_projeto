from pydantic import BaseModel, StringConstraints, condecimal
from datetime import datetime
from typing import Annotated

class TransacaoCreate(BaseModel):
    descricao: str
    valor: float
    tipo: Annotated[str, StringConstraints(to_lower=True, pattern="^(crédito|débito)$")]
    data: datetime

class TransacaoRead(TransacaoCreate):
    id: int

    class Config:
        orm_mode = True