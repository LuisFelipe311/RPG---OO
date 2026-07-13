import customtkinter as ctk

from tela_inicial import TelaInicial
from tela_criacao import TelaCriacaoPersonagem
from tela_hub import TelaHub
from tela_combate import TelaCombate
from tela_fim import TelaFim

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Crônicas de Aetherion")
        self.geometry("900x650")
        self.resizable(False, False)

        self.personagem = None
        self.encontro_atual = 0
        self.inimigo_atual = None
        self.missao_atual = None

        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)

        self.frames = {}
        for Tela in (TelaInicial, TelaCriacaoPersonagem, TelaHub, TelaCombate, TelaFim):
            frame = Tela(self.container, self)
            self.frames[Tela.__name__] = frame
            frame.place(relwidth=1, relheight=1)

        self.mostrar_tela("TelaInicial")

    def mostrar_tela(self, nome: str):
        frame = self.frames[nome]
        frame.tkraise()
        if hasattr(frame, "ao_mostrar"):
            frame.ao_mostrar()


if __name__ == "__main__":
    app = App()
    app.mainloop()