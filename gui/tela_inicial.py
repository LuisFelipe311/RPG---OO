"""Tela inicial - Novo Jogo ou Carregar Jogo."""
import customtkinter as ctk
from persistencia import existe_save, carregar_jogo


class TelaInicial(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app

        ctk.CTkLabel(self, text="Crônicas de Aetherion",
                     font=("Georgia", 32, "bold")).pack(pady=(80, 10))
        ctk.CTkLabel(self, text="O reino de Aetherion aguarda um herói.",
                     font=("Georgia", 16)).pack(pady=(0, 40))

        ctk.CTkButton(self, text="Novo Jogo", width=220, height=45,
                      command=self.novo_jogo).pack(pady=10)

        self.btn_carregar = ctk.CTkButton(self, text="Carregar Jogo", width=220, height=45,
                                           command=self.carregar)
        self.btn_carregar.pack(pady=10)

    def ao_mostrar(self):
        self.btn_carregar.configure(state="normal" if existe_save() else "disabled")

    def novo_jogo(self):
        self.app.mostrar_tela("TelaCriacaoPersonagem")

    def carregar(self):
        resultado = carregar_jogo()
        if resultado is None:
            return
        personagem, encontro_atual = resultado
        self.app.personagem = personagem
        self.app.encontro_atual = encontro_atual
        self.app.mostrar_tela("TelaHub")