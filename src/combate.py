"""Classe Combate - coordena o embate entre dois Personagens."""
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from personagem import Personagem


class Combate:
    def __init__(self, personagem_a: "Personagem", personagem_b: "Personagem"):
        self.personagem_a = personagem_a
        self.personagem_b = personagem_b
        self.turno_atual = 0
        self.em_andamento = False

    def iniciar_combate(self) -> None:
        """Inicia o laço de turnos até que um dos personagens seja derrotado."""
        self.em_andamento = True
        print(f"Combate iniciado: {self.personagem_a.nome} vs {self.personagem_b.nome}")
        while self.em_andamento:
            self.executar_turno()

    def executar_turno(self) -> None:
        """Executa um turno: cada personagem vivo ataca o outro, na ordem A -> B."""
        self.turno_atual += 1
        print(f"--- Turno {self.turno_atual} ---")

        if self.personagem_a.esta_vivo():
            self.personagem_a.atacar(self.personagem_b)
        if self.personagem_b.esta_vivo():
            self.personagem_b.atacar(self.personagem_a)

        if not self.personagem_a.esta_vivo() or not self.personagem_b.esta_vivo():
            self.finalizar_combate()

    def finalizar_combate(self) -> None:
        """Encerra o combate e anuncia o vencedor."""
        self.em_andamento = False
        vencedor = self.personagem_a if self.personagem_a.esta_vivo() else self.personagem_b
        print(f"Combate finalizado! Vencedor: {vencedor.nome}")