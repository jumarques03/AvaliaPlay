from fastapi import FastAPI
from metodos.avaliação import Avaliacao

app = FastAPI()

jogos = []

@app.post("/adicionar/jogo")
def adicionar_jogo(jogo: Avaliacao):
    for jogo_existente in jogos:
        if jogo_existente.nome == jogo.nome:
            return {"mensagem": "Já existe este jogo em nosso site!"}

    jogos.append(jogo)
    return {"mensagem": "Jogo adicionado!", "jogo": jogo}

@app.get("/jogos")
def listar_jogos():
    if not jogos:
        return {"mensagem": "Não há nenhum jogo em nossa lista!"}
    else: 
        return {"jogos": jogos}