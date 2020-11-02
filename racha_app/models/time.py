class Time:

    id = None
    nome = None
    jogadores = None
    pontos = None

    def __init__(self, nome, jogadores, pontos):
        self.nome = nome
        self.jogadores = jogadores
        self.pontos = pontos