from fastapi import FastAPI
from metodos.descricao import Descricao
from metodos.avaliação import Avaliacao

app = FastAPI()

jogos = []
avaliacoes=[]

@app.post("/adicionar/jogo")
def adicionar_jogo(jogo: Descricao):
    for jogo_existente in jogos:
        if jogo_existente.nome == jogo.nome:
            return {"mensagem": "Já existe este jogo em nosso site!"}

    jogos.append(jogo)
    return {"mensagem": "Jogo adicionado!", "jogo": jogo}

@app.get("/jogos")
def listar_jogos():
    lista_jogos_com_avaliacao=[]

    if not jogos:
        return {"mensagem": "Não há nenhum jogo em nossa lista!"}
    
    for jogo_existente in jogos:
        jogo_avaliacoes=[]
        soma_avaliacoes = 0
        total_avaliacoes = 0

        for avaliacao in avaliacoes:
            if avaliacao.nome_jogo == jogo_existente.nome:
                jogo_avaliacoes.append(avaliacao)
                soma_avaliacoes += avaliacao.nota
                total_avaliacoes += 1
        
        if total_avaliacoes > 0:
            media_avaliacoes = soma_avaliacoes / total_avaliacoes
        else:
            media_avaliacoes = None

        lista_jogos_com_avaliacao.append({
            "jogo": jogo_existente,
            "avaliacoes": jogo_avaliacoes,
            "media_avaliacoes": media_avaliacoes
        })

    return {"jogos": lista_jogos_com_avaliacao}

@app.post("/adicionar/avaliacao")
def adicionar_avaliacao(avaliacao: Avaliacao):
    for jogo_existente in jogos:
        if jogo_existente.nome == avaliacao.nome_jogo:
            avaliacoes.append(avaliacao)
            return {"avaliações": avaliacao}
    
    return{"mensagem": "Esse jogo não existe em nosso site! Adicione-o para avaliá-lo!"}