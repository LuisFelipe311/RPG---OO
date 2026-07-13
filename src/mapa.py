"""Classes Mapa, Sala e Evento."""
from __future__ import annotations
import random
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from personagem import Personagem


class Evento:
    def __init__(self, tipo: str, descricao: str):
        self.tipo = tipo
        self.descricao = descricao

    def acionar(self, personagem: "Personagem") -> None:
        """Aplica o efeito do evento sobre o personagem (armadilha, tesouro, emboscada...)."""
        print(f"Evento '{self.tipo}' acionado para {personagem.nome}: {self.descricao}")
        if self.tipo == "armadilha":
            personagem.receber_dano(random.randint(1, 5))
        elif self.tipo == "cura":
            personagem.recuperar_saude(random.randint(1, 5))


class Sala:
    def __init__(self, nome: str, descricao: str):
        self.nome = nome
        self.descricao = descricao
        self.eventos: List[Evento] = []
        self.inimigos_presentes: list = []

    def adicionar_evento(self, evento: Evento) -> None:
        self.eventos.append(evento)

    def entrar(self, personagem: "Personagem") -> None:
        """Ao entrar na sala, há chance de acionar um evento aleatório."""
        print(f"{personagem.nome} entrou em '{self.nome}': {self.descricao}")
        if self.eventos and random.random() < 0.5:  # 50% de chance de evento
            evento = random.choice(self.eventos)
            evento.acionar(personagem)


class Mapa:
    def __init__(self, nome: str):
        self.nome = nome
        self.salas: List[Sala] = []

    def adicionar_sala(self, sala: Sala) -> None:
        self.salas.append(sala)

    def navegar_para(self, nome_sala: str) -> Sala | None:
        """Retorna a sala pelo nome, se existir no mapa."""
        for sala in self.salas:
            if sala.nome == nome_sala:
                return sala
        print(f"Sala '{nome_sala}' não encontrada no mapa '{self.nome}'.")
        return None