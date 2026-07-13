"""Classe Jogador - controla um PersonagemJogador."""
from __future__ import annotations
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from personagem_jogador import PersonagemJogador # pyright: ignore[reportMissingImports]


class Jogador:
    def __init__(self, nome: str):
        self.nome = nome
        self.personagem: Optional["PersonagemJogador"] = None

    def escolher_personagem(self, personagem: "PersonagemJogador") -> None:
        """Associa um PersonagemJogador a este jogador."""
        self.personagem = personagem
        print(f"{self.nome} está controlando {personagem.nome}.")

    def realizar_jogada(self) -> None:
        if self.personagem is None:
            print(f"{self.nome} ainda não escolheu um personagem.")
            return
        print(f"{self.nome} realiza uma jogada com {self.personagem.nome}.")

    def __repr__(self):
        return f"Jogador(nome='{self.nome}', personagem={self.personagem})"