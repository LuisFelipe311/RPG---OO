"""Tela de criação de personagem."""
import customtkinter as ctk
from dado import Dado
from personagem_jogador import PersonagemJogador, ClassePersonagem
from item import Arma, Pocao


class TelaCriacaoPersonagem(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self._dado = Dado()
        self._atributos = None

        ctk.CTkLabel(self, text="Criação de Personagem",
                     font=("Georgia", 26, "bold")).pack(pady=(40, 20))

        ctk.CTkLabel(self, text="Nome do personagem:").pack()
        self.entry_nome = ctk.CTkEntry(self, width=250, placeholder_text="Ex: Kael")
        self.entry_nome.pack(pady=(0, 15))

        ctk.CTkLabel(self, text="Classe:").pack()
        self.combo_classe = ctk.CTkOptionMenu(self, values=["Guerreiro", "Mago", "Ladino"])
        self.combo_classe.pack(pady=(0, 15))

        self.label_atributos = ctk.CTkLabel(self, text="", font=("Consolas", 14), justify="left")
        self.label_atributos.pack(pady=15)

        ctk.CTkButton(self, text="Rolar Atributos", command=self.rolar_atributos).pack(pady=5)

        self.btn_confirmar = ctk.CTkButton(self, text="Começar Jornada",
                                            command=self.confirmar, state="disabled")
        self.btn_confirmar.pack(pady=20)

    def ao_mostrar(self):
        self.rolar_atributos()

    def rolar_atributos(self):
        # Cada atributo é a soma de 3 dados de 6 faces, seguindo a mesma regra dos testes
        forca = sum(self._dado.rolar() for _ in range(3))
        inteligencia = sum(self._dado.rolar() for _ in range(3))
        saude = sum(self._dado.rolar() for _ in range(3))
        self._atributos = {
            "forca": forca, "inteligencia": inteligencia, "saude": saude,
            "nh_fisico": forca + 3, "nh_mental": inteligencia + 3,
        }
        self.label_atributos.configure(
            text=(f"Força: {forca}    Inteligência: {inteligencia}    Saúde: {saude}\n"
                  f"NH Físico: {self._atributos['nh_fisico']}    "
                  f"NH Mental: {self._atributos['nh_mental']}")
        )
        self.btn_confirmar.configure(state="normal")

    def confirmar(self):
        nome = self.entry_nome.get().strip() or "Aventureiro"
        classe = ClassePersonagem[self.combo_classe.get().upper()]

        personagem = PersonagemJogador(nome=nome, classe=classe, **self._atributos)

        # Equipamento inicial
        espada = Arma("Espada Curta", "Uma lâmina simples, porém afiada", valor=10, dano=5)
        pocao = Pocao("Poção de Cura", "Restaura vida", valor=5, cura_quantidade=6)
        personagem.inventario.adicionar_item(espada)
        personagem.inventario.adicionar_item(pocao)
        personagem.usar_item(espada)  # equipa a arma automaticamente

        self.app.personagem = personagem
        self.app.encontro_atual = 0
        self.app.mostrar_tela("TelaHub")