"""Classe abstrata Personagem - base para PersonagemJogador e Inimigo."""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional, TYPE_CHECKING

from inventario import Inventario
from teste_habilidade import TesteHabilidade

if TYPE_CHECKING:
    from item import Item, Arma, Armadura


class Personagem(ABC):
    def __init__(self, nome: str, forca: int, inteligencia: int, saude: int,
                 nh_fisico: int, nh_mental: int):
        assert 3 <= forca <= 18, "Força deve estar entre 3 e 18"
        assert 3 <= inteligencia <= 18, "Inteligência deve estar entre 3 e 18"
        assert 3 <= saude <= 18, "Saúde deve estar entre 3 e 18"

        self.nome = nome
        self.forca = forca
        self.inteligencia = inteligencia
        self.saude = saude
        self.nh_fisico = nh_fisico
        self.nh_mental = nh_mental
        self.pontos_de_vida = saude  # PV inicial = saúde
        self.inventario = Inventario()

        self.arma_equipada: Optional["Arma"] = None
        self.armadura_equipada: Optional["Armadura"] = None

    def atacar(self, alvo: "Personagem") -> None:
        """Realiza um teste físico; se bem-sucedido, aplica dano ao alvo."""
        sucesso = self.realizar_teste_fisico()
        if sucesso:
            dano_base = self.arma_equipada.calcular_dano() if self.arma_equipada else 1
            print(f"{self.nome} acertou o ataque contra {alvo.nome}!")
            alvo.receber_dano(dano_base)
        else:
            print(f"{self.nome} errou o ataque contra {alvo.nome}.")

    def defender(self) -> int:
        """Retorna o valor de redução de dano vindo da armadura equipada."""
        return self.armadura_equipada.calcular_defesa() if self.armadura_equipada else 0

    def usar_item(self, item: "Item") -> None:
        """Usa um item do inventário (poção cura, arma/armadura equipa)."""
        if item not in self.inventario.itens:
            print(f"{self.nome} não possui {item.nome} no inventário.")
            return
        item.usar(self)

    def realizar_teste_fisico(self) -> bool:
        """Executa um TesteHabilidade contra o NH Físico."""
        teste = TesteHabilidade(self, "fisico", self.nh_fisico)
        teste.executar_teste()
        return teste.verificar_sucesso()

    def realizar_teste_mental(self) -> bool:
        """Executa um TesteHabilidade contra o NH Mental."""
        teste = TesteHabilidade(self, "mental", self.nh_mental)
        teste.executar_teste()
        return teste.verificar_sucesso()

    def receber_dano(self, valor: int) -> None:
        """Reduz o dano pela defesa da armadura e subtrai dos pontos de vida."""
        dano_efetivo = max(0, valor - self.defender())
        self.pontos_de_vida = max(0, self.pontos_de_vida - dano_efetivo)
        print(f"{self.nome} recebeu {dano_efetivo} de dano (PV: {self.pontos_de_vida}).")

    def recuperar_saude(self, valor: int) -> None:
        """Restaura pontos de vida, sem ultrapassar a saúde máxima."""
        self.pontos_de_vida = min(self.saude, self.pontos_de_vida + valor)

    def esta_vivo(self) -> bool:
        """Retorna True enquanto os pontos de vida forem maiores que zero."""
        return self.pontos_de_vida > 0

    def __repr__(self):
        return f"{self.__class__.__name__}(nome='{self.nome}', PV={self.pontos_de_vida}/{self.saude})"