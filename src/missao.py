"""Classe Missao (ou Objetivo) - envolve inimigos e concede recompensas."""
from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from inimigo import Inimigo
    from personagem_jogador import PersonagemJogador # pyright: ignore[reportMissingImports]


class Missao:
    def __init__(self, nome: str, descricao: str, recompensa: str):
        self.nome = nome
        self.descricao = descricao
        self.recompensa = recompensa
        self.concluida = False
        self.inimigos_associados: List["Inimigo"] = []

    def adicionar_inimigo(self, inimigo: "Inimigo") -> None:
        """Associa um inimigo que precisa ser derrotado para concluir a missão."""
        self.inimigos_associados.append(inimigo)

    def verificar_conclusao(self) -> bool:
        """A missão é concluída quando todos os inimigos associados não estão mais vivos."""
        self.concluida = all(not inimigo.esta_vivo() for inimigo in self.inimigos_associados)
        return self.concluida

    def conceder_recompensa(self, personagem: "PersonagemJogador") -> None:
        """Concede XP/recompensa ao personagem se a missão estiver concluída."""
        if not self.concluida:
            print(f"Missão '{self.nome}' ainda não foi concluída.")
            return
        print(f"{personagem.nome} recebeu a recompensa: {self.recompensa}")
        personagem.ganhar_xp(50)

    def __repr__(self):
        status = "concluída" if self.concluida else "em andamento"
        return f"Missao(nome='{self.nome}', status={status})"