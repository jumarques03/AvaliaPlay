from fastapi import FastAPI
from rotas.rotas import rota

app = FastAPI()
app.include_router(rota)

