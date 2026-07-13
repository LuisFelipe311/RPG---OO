"""Enum ClassePersonagem e classe PersonagemJogador (herda de Personagem)."""
from __future__ import annotations
from enum import Enum, auto

from personagem import Personagem


class ClassePersonagem(Enum):
    GUERREIRO = auto()
    MAGO = auto()
    LADINO = auto()


class PersonagemJogador(Personagem):
    XP_POR_NIVEL = 100

    def __init__(self, nome: str, forca: int, inteligencia: int, saude: int,
                 nh_fisico: int, nh_mental: int, classe: ClassePersonagem):
        super().__init__(nome, forca, inteligencia, saude, nh_fisico, nh_mental)
        self.classe = classe
        self.experiencia = 0
        self.nivel = 1

    def ganhar_xp(self, quantidade: int) -> None:
        """Adiciona experiência e evolui de nível automaticamente se atingir o limiar."""
        self.experiencia += quantidade
        if self.experiencia >= self.XP_POR_NIVEL:
            self.experiencia -= self.XP_POR_NIVEL
            self.evoluir()

    def evoluir(self) -> None:
        """Sobe de nível e aumenta um atributo conforme a classe do personagem."""
        self.nivel += 1
        if self.classe == ClassePersonagem.GUERREIRO:
            self.forca += 1
        elif self.classe == ClassePersonagem.MAGO:
            self.inteligencia += 1
        else:  # LADINO
            self.nh_fisico = max(3, self.nh_fisico - 1)  # fica mais difícil de falhar
        print(f"{self.nome} subiu para o nível {self.nivel}!")