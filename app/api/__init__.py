from fastapi import APIRouter
from .transacoes import router as transacoes_router

router = APIRouter()
router.include_router(transacoes_router, prefix="/transacoes", tags=["Transações"])