from pydantic import BaseModel

class Jogo(BaseModel):
    nome: str
    categoria: str