"""Classe abstrata Item e suas especializações: Arma, Armadura, Pocao."""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from personagem import Personagem


class Item(ABC):
    def __init__(self, nome: str, descricao: str, valor: int):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

    @abstractmethod
    def usar(self, personagem: "Personagem") -> None:
        """Aplica o efeito do item sobre o personagem. Implementado pelas subclasses."""
        raise NotImplementedError

    def __repr__(self):
        return f"{self.__class__.__name__}(nome='{self.nome}', valor={self.valor})"


class Arma(Item):
    def __init__(self, nome: str, descricao: str, valor: int, dano: int):
        super().__init__(nome, descricao, valor)
        self.dano = dano

    def calcular_dano(self) -> int:
        """Retorna o dano base da arma."""
        return self.dano

    def usar(self, personagem: "Personagem") -> None:
        """Equipa a arma no personagem; o dano passa a ser aplicado em atacar()."""
        personagem.arma_equipada = self
        print(f"{personagem.nome} equipou {self.nome} (dano {self.dano}).")


class Armadura(Item):
    def __init__(self, nome: str, descricao: str, valor: int, defesa: int):
        super().__init__(nome, descricao, valor)
        self.defesa = defesa

    def calcular_defesa(self) -> int:
        """Retorna o valor de defesa da armadura."""
        return self.defesa

    def usar(self, personagem: "Personagem") -> None:
        """Equipa a armadura no personagem; a defesa passa a ser aplicada em defender()."""
        personagem.armadura_equipada = self
        print(f"{personagem.nome} equipou {self.nome} (defesa {self.defesa}).")


class Pocao(Item):
    def __init__(self, nome: str, descricao: str, valor: int, cura_quantidade: int):
        super().__init__(nome, descricao, valor)
        self.cura_quantidade = cura_quantidade

    def aplicar_cura(self, personagem: "Personagem") -> None:
        """Restaura pontos de vida do personagem, sem passar do máximo."""
        personagem.recuperar_saude(self.cura_quantidade)

    def usar(self, personagem: "Personagem") -> None:
        """Usar a poção aplica a cura imediatamente e a consome."""
        self.aplicar_cura(personagem)
        if self in personagem.inventario.itens:
            personagem.inventario.remover_item(self)
        print(f"{personagem.nome} usou {self.nome} e recuperou {self.cura_quantidade} de vida.")