import os
import customtkinter as ctk


class TelaFim(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app

        self.label_resultado = ctk.CTkLabel(self, text="", font=("Georgia", 30, "bold"))
        self.label_resultado.pack(pady=(120, 10))

        self.label_mensagem = ctk.CTkLabel(self, text="", font=("Georgia", 16),
                                            wraplength=500, justify="center")
        self.label_mensagem.pack(pady=10)

        ctk.CTkButton(self, text="Jogar Novamente", width=220, height=45,
                      command=self.reiniciar).pack(pady=30)

    def ao_mostrar(self):
        personagem = self.app.personagem
        if personagem and personagem.esta_vivo():
            self.label_resultado.configure(text="🏆 VITÓRIA!", text_color="#f1c40f")
            self.label_mensagem.configure(
                text=f"{personagem.nome} derrotou Malachar e salvou o reino de Aetherion!"
            )
        else:
            self.label_resultado.configure(text="💀 DERROTA", text_color="#e74c3c")
            self.label_mensagem.configure(
                text="Sua jornada termina aqui. Aetherion permanece nas trevas... por enquanto."
            )

        if os.path.exists("save.json"):
            os.remove("save.json")

    def reiniciar(self):
        self.app.personagem = None
        self.app.encontro_atual = 0
        self.app.mostrar_tela("TelaInicial")