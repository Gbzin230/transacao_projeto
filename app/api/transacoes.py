from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.base import get_db
from app.db.models import Transacao
from app.schemas.transacao import TransacaoCreate, TransacaoRead
from datetime import datetime
from typing import List
import csv
import os

CSV_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "transacoes.csv")
CSV_PATH = os.path.abspath(CSV_PATH)

router = APIRouter()

@router.post("/", response_model=TransacaoRead)
def criar_transacao(transacao: TransacaoCreate, db: Session = Depends(get_db)):
    nova = Transacao(**transacao.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)

    escrever_csv(nova)

    return nova

def escrever_csv(transacao: Transacao):
    file_exists = os.path.isfile(CSV_PATH)
    with open(CSV_PATH, mode='a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(["data", "descricao", "tipo", "valor"])
        writer.writerow([transacao.data, transacao.descricao, transacao.tipo, transacao.valor])



@router.get("/", response_model=list[TransacaoRead])
def listar_transacoes(db: Session = Depends(get_db)):
    return db.query(Transacao).all()