"""Classe Dado - representa um dado de seis faces usado nos testes de habilidade."""
import random


class Dado:
    def __init__(self, faces: int = 6):
        self.faces = faces

    def rolar(self) -> int:
        """Lança o dado e retorna um valor entre 1 e o número de faces."""
        return random.randint(1, self.faces)

    def __repr__(self):
        return f"Dado(faces={self.faces})"