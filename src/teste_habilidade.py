"""Classe TesteHabilidade - resolve testes de sorte/habilidade com 3 dados de 6 faces."""
from __future__ import annotations
from typing import TYPE_CHECKING, List

from dado import Dado

if TYPE_CHECKING:
    from personagem import Personagem


class TesteHabilidade:
    def __init__(self, personagem: "Personagem", atributo_testado: str, valor_alvo: int):
        
        self.personagem = personagem
        self.atributo_testado = atributo_testado
        self.valor_alvo = valor_alvo
        self.dados: List[Dado] = [Dado(), Dado(), Dado()]
        self.resultado_dados: int = 0

    def executar_teste(self) -> int:
        """Rola os 3 dados e guarda a soma como resultado do teste."""
        self.resultado_dados = sum(dado.rolar() for dado in self.dados)
        return self.resultado_dados

    def verificar_sucesso(self) -> bool:
        """Regra do jogo: sucesso se a soma dos dados for MENOR que o NH correspondente."""
        return self.resultado_dados < self.valor_alvo

    def __repr__(self):
        return (f"TesteHabilidade(atributo='{self.atributo_testado}', "
                f"resultado={self.resultado_dados}, alvo={self.valor_alvo})")