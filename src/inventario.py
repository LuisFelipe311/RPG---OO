"""Classe Inventario - armazena os itens de um personagem."""
from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from item import Item


class Inventario:
    def __init__(self, capacidade_maxima: int = 10):
        self.capacidade_maxima = capacidade_maxima
        self.itens: List["Item"] = []

    def adicionar_item(self, item: "Item") -> bool:
        """Adiciona um item se houver espaço. Retorna True se conseguiu adicionar."""
        if len(self.itens) >= self.capacidade_maxima:
            print("Inventário cheio!")
            return False
        self.itens.append(item)
        return True

    def remover_item(self, item: "Item") -> bool:
        """Remove um item do inventário. Retorna True se o item existia."""
        if item in self.itens:
            self.itens.remove(item)
            return True
        return False

    def listar_itens(self) -> List["Item"]:
        """Retorna a lista de itens presentes no inventário."""
        return self.itens

    def __repr__(self):
        return f"Inventario({len(self.itens)}/{self.capacidade_maxima} itens)"