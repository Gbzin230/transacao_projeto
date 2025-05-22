# Projeto de Controle de Transações Financeiras

Este projeto é uma aplicação simples para gerenciar transações financeiras, composta por uma API REST feita com FastAPI, um banco de dados SQLite e um dashboard interativo criado com Streamlit.

## Funcionalidades

- **API REST** para criação e listagem de transações financeiras (crédito/débito).
- **Persistência dos dados** usando SQLite via SQLAlchemy.
- **Dashboard visual** para exibir as transações e o total movimentado, lendo os dados de um arquivo CSV gerado pela API.



## Como usar

### Instalação

1. Clone o repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

2. Crie e ative o ambiente virtual:

python -m venv .venv
source .venv/bin/activate      # Linux/macOS
.venv\Scripts\activate         # Windows

4. Instale as dependências:

pip install -r requirements.txt

5. Rodar a API

uvicorn main:app --reload
A API estará disponível em: http://127.0.0.1:8000

6. Rodar o Dashboard

Em outro terminal, execute:
streamlit run dashboard/app.py
O dashboard abrirá no navegador, exibindo as transações presentes no CSV.

7. Testando a API

Você pode usar ferramentas como **Insomnia** para enviar requisições.

8. Exemplo para criar uma transação:

Método: **POST**
URL: http://127.0.0.1:8000/api/transacoes/
**Body (JSON):**
{
  "data": "2025-05-21T14:30:00",
  "descricao": "Compra mercado",
  "tipo": "débito",
  "valor": 150.5
}

## Tecnologias
FastAPI

SQLAlchemy

Pydantic

Streamlit

SQLite

## Contribuição
Contribuições são bem-vindas! Abra issues ou envie pull requests.
