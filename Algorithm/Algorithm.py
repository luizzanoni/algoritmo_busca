from abc import abstractmethod

from Problem.Jogo8.Acao import Acao
from Problem.Jogo8.Estado import Estado
from Problem.Jogo8.Jogo8 import Jogo8
from Tree.Arvore import Arvore


class Algorithm:
    def __init__(self, nome: str, arvore_busca: Arvore, objetivo: Estado):
        self.nome: str = nome
        self.arvore_busca: Arvore = arvore_busca
        self.objetivo: Estado = objetivo
        self.solucao: list[int] | None = None
        self.tempo_execucao: float = 0.0
        self.estados_analisados: int = 0
        self.ramificacao: int = 0

    @abstractmethod
    def encontrar_solucao(self):
        pass

    def expandir(self, arvore: Arvore) -> list[Arvore]:
        estados_expandidos = []
        for acao in Acao:
            # Otimização — Não repetir ação inversa da última usada
            if arvore.pai is None or acao != arvore.acao.inversa():
                novo_estado = Jogo8.transicao(arvore.estado, acao)
                # Testa se a ação foi válida
                if novo_estado != arvore.estado:
                    self.ramificacao += 1
                    estados_expandidos.append(arvore.adicionar_filho(novo_estado, acao))
        return estados_expandidos

    def eh_objetivo(self, estado_atual: Estado) -> bool:
        return estado_atual == self.objetivo
