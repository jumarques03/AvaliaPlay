import json

def salvar_lista_jogos(lista):
    """
    Função responsável por salvar a lista de jogos.
    """
    try:
        with open('jogos_salvos.json', 'w') as f:
            json.dump(lista, f, indent=4)
    except PermissionError as erro:
        raise erro