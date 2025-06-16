from fastapi import FastAPI
from metodos.descricao import Descricao

app = FastAPI()

jogos = []

@app.post("/adicionar/jogo")
def adicionar_jogo(jogo: Descricao ):
    jogos.append(jogo)
    return {"mensagem": "Jogo adicionado!", "jogo": jogo}

@app.get("/jogos")
def listar_jogos():
    return {"jogos": jogos}