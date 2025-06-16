from pydantic import BaseModel

class Avaliacao(BaseModel):
    nota: int
    comentario: str

class NovaAvaliacao(BaseModel):
    nome: str
    nota: int
    cometario: str

