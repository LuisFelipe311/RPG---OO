"""Classe Inimigo (herda de Personagem)."""
from __future__ import annotations
import random

from personagem import Personagem


class Inimigo(Personagem):
    def __init__(self, nome: str, forca: int, inteligencia: int, saude: int,
                 nh_fisico: int, nh_mental: int, tipo_inimigo: str, recompensa_xp: int):
        super().__init__(nome, forca, inteligencia, saude, nh_fisico, nh_mental)
        self.tipo_inimigo = tipo_inimigo
        self.recompensa_xp = recompensa_xp

    def definir_comportamento(self) -> str:
        """Define de forma simples a ação do inimigo no turno (IA básica)."""
        acao = random.choice(["atacar", "defender"])
        return acao