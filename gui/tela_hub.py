"""Tela hub - status do personagem e navegação pelas salas da torre."""
import customtkinter as ctk
from encontros import criar_encontros
from persistencia import salvar_jogo


class TelaHub(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.encontros = criar_encontros()

        self.label_titulo = ctk.CTkLabel(self, text="", font=("Georgia", 24, "bold"))
        self.label_titulo.pack(pady=(30, 5))

        self.label_status = ctk.CTkLabel(self, text="", font=("Consolas", 14), justify="left")
        self.label_status.pack(pady=10)

        self.label_sala = ctk.CTkLabel(self, text="", font=("Georgia", 15),
                                        wraplength=600, justify="center")
        self.label_sala.pack(pady=20)

        self.log = ctk.CTkTextbox(self, width=650, height=120, state="disabled")
        self.log.pack(pady=10)

        botoes = ctk.CTkFrame(self, fg_color="transparent")
        botoes.pack(pady=15)
        ctk.CTkButton(botoes, text="Entrar na Sala", width=180,
                      command=self.entrar_na_sala).grid(row=0, column=0, padx=8)
        ctk.CTkButton(botoes, text="Salvar Jogo", width=140,
                      command=self.salvar).grid(row=0, column=1, padx=8)

    def ao_mostrar(self):
        self._atualizar_status()
        encontro = self._encontro_atual()
        if encontro:
            self.label_sala.configure(
                text=f"📍 {encontro['sala'].nome}\n{encontro['sala'].descricao}"
            )
        self._log("Bem-vindo de volta, aventureiro.")

    def _encontro_atual(self):
        if self.app.encontro_atual >= len(self.encontros):
            return None
        return self.encontros[self.app.encontro_atual]

    def _atualizar_status(self):
        p = self.app.personagem
        self.label_titulo.configure(text=f"{p.nome} — {p.classe.name.capitalize()} (Nível {p.nivel})")
        self.label_status.configure(
            text=(f"PV: {p.pontos_de_vida}/{p.saude}    Força: {p.forca}    "
                  f"Inteligência: {p.inteligencia}    XP: {p.experiencia}")
        )

    def _log(self, texto: str):
        self.log.configure(state="normal")
        self.log.insert("end", texto + "\n")
        self.log.see("end")
        self.log.configure(state="disabled")

    def entrar_na_sala(self):
        encontro = self._encontro_atual()
        if encontro is None:
            return
        sala = encontro["sala"]
        personagem = self.app.personagem

        pv_antes = personagem.pontos_de_vida
        sala.entrar(personagem)
        if personagem.pontos_de_vida != pv_antes:
            self._log(f"Um evento ocorreu na sala '{sala.nome}'.")
            self._atualizar_status()

        if not personagem.esta_vivo():
            self.app.mostrar_tela("TelaFim")
            return

        inimigo = encontro["inimigo"]
        if inimigo.esta_vivo():
            self.app.inimigo_atual = inimigo
            self.app.missao_atual = encontro["missao"]
            self.app.mostrar_tela("TelaCombate")
        else:
            self.avancar_encontro()

    def avancar_encontro(self):
        self.app.encontro_atual += 1
        if self.app.encontro_atual >= len(self.encontros):
            self.app.mostrar_tela("TelaFim")
        else:
            self.ao_mostrar()

    def salvar(self):
        salvar_jogo(self.app.personagem, self.app.encontro_atual)
        self._log("Jogo salvo com sucesso!")