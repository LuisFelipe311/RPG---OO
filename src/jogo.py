"""Classe Jogo - orquestra jogadores, missões e o mapa."""
from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from jogador import Jogador
    from missao import Missao
    from mapa import Mapa # pyright: ignore[reportMissingImports]


class Jogo:
    def __init__(self, nome: str, cenario: str, historia: str, objetivo_principal: str, mapa: "Mapa"):
        self.nome = nome
        self.cenario = cenario
        self.historia = historia
        self.objetivo_principal = objetivo_principal
        self.mapa = mapa
        self.jogadores: List["Jogador"] = []
        self.missoes: List["Missao"] = []

    def adicionar_jogador(self, jogador: "Jogador") -> None:
        """Adiciona um jogador à partida."""
        self.jogadores.append(jogador)

    def adicionar_missao(self, missao: "Missao") -> None:
        """Adiciona uma missão ao jogo."""
        self.missoes.append(missao)

    def iniciar_jogo(self) -> None:
        """Exibe a introdução do jogo."""
        print(f"=== {self.nome} ===")
        print(f"Cenário: {self.cenario}")
        print(f"História: {self.historia}")
        print(f"Objetivo: {self.objetivo_principal}\n")

    def verificar_vitoria(self) -> bool:
        """Vitória quando todas as missões estão concluídas."""
        return all(missao.concluida for missao in self.missoes) and len(self.missoes) > 0

    def verificar_derrota(self) -> bool:
        """Derrota quando todos os personagens dos jogadores estão mortos."""
        personagens = [j.personagem for j in self.jogadores if j.personagem is not None]
        if not personagens:
            return False
        return all(not p.esta_vivo() for p in personagens)

    def __repr__(self):
        return f"Jogo(nome='{self.nome}', jogadores={len(self.jogadores)}, missoes={len(self.missoes)})"