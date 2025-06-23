from fastapi import APIRouter,HTTPException
from metodos.descricao import Descricao
from metodos.avaliação import Avaliacao
from rotas.funcs_auxiliares import salvar_lista_jogos

rota=APIRouter()

jogos = []
avaliacoes=[]
    
@rota.post("/adicionar/jogo")
async def adicionar_jogo(jogo: Descricao):
    """
    Função que permite o usuário adicionar um jogo à lista de jogos.
    """
    for jogo_existente in jogos:
        if jogo_existente.nome == jogo.nome:
            return {"mensagem": "Já existe este jogo em nosso site!"}

    jogos.append(jogo)
    return {"mensagem": "Jogo adicionado!", "jogo": jogo}

@rota.get("/jogos")
async def listar_jogos():
    """
    Função que permite a listagem dos jogos e suas avaliações
    """
    try:
        lista_jogos_com_avaliacao=[]

        if not jogos:
            return {"mensagem": "Não há nenhum jogo em nossa lista!"}
        
        for jogo_existente in jogos:
            jogo_avaliacoes=[]
            soma_avaliacoes = 0
            total_avaliacoes = 0

            for avaliacao in avaliacoes:
                if avaliacao.nome_jogo == jogo_existente.nome:
                    jogo_avaliacoes.append(avaliacao.dict())
                    soma_avaliacoes += avaliacao.nota
                    total_avaliacoes += 1
            
            if total_avaliacoes > 0:
                media_avaliacoes = soma_avaliacoes / total_avaliacoes
            else:
                media_avaliacoes = None

            lista_jogos_com_avaliacao.append({
                "jogo": jogo_existente.dict(),
                "avaliacoes": jogo_avaliacoes,
                "media_avaliacoes": media_avaliacoes
            })

        salvar_lista_jogos(lista_jogos_com_avaliacao)
        return {"jogos": lista_jogos_com_avaliacao}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao listar jogos: {str(e)}")

@rota.post("/adicionar/avaliacao")
async def adicionar_avaliacao(avaliacao: Avaliacao):
    """
    Função que permite o usuário adicionar uma avaliação à um jogo específico
    """
    for jogo_existente in jogos:
        if jogo_existente.nome == avaliacao.nome_jogo:
            avaliacoes.append(avaliacao)
            return {"avaliações": avaliacao}
    
    raise HTTPException(status_code=404, detail="Este jogo ainda não existe em nossa lista. Adicione-o para avaliá-lo!")
