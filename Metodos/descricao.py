from metodos.jogo import Jogo
from metodos.avaliação import Avaliacao
from typing import List

class Descricao(Jogo):
    descricao: str
    avaliacoes: List[Avaliacao]