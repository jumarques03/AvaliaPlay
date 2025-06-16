from pydantic import BaseModel

class Avaliacao(BaseModel):
    nome_jogo: str
    nota: int
    comentario: str


