from fastapi import FastAPI
from metodos.avaliação import Avaliacao

app = FastAPI()

jogos = []

@app.post("/adicionar/jogo")
def adicionar_jogo(jogo: Avaliacao):
    jogos.append(jogo)
    return {"mensagem": "Jogo adicionado!", "jogo": jogo}

@app.get("/jogos")
def listar_jogos():
    return {"jogos": jogos}