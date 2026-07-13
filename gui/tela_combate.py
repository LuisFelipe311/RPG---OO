"""Tela de combate - turnos disparados por clique, reaproveitando a classe Combate."""
import io
import contextlib
import customtkinter as ctk
from combate import Combate


class TelaCombate(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.combate = None

        self.label_inimigo = ctk.CTkLabel(self, text="", font=("Georgia", 22, "bold"))
        self.label_inimigo.pack(pady=(30, 5))

        self.label_pv = ctk.CTkLabel(self, text="", font=("Consolas", 15))
        self.label_pv.pack(pady=10)

        self.log = ctk.CTkTextbox(self, width=650, height=250, state="disabled")
        self.log.pack(pady=15)

        self.btn_atacar = ctk.CTkButton(self, text="⚔ Atacar!", width=200, height=45,
                                         command=self.atacar)
        self.btn_atacar.pack(pady=10)

        self.btn_continuar = ctk.CTkButton(self, text="Continuar", width=200,
                                            command=self.continuar)

    def ao_mostrar(self):
        inimigo = self.app.inimigo_atual
        personagem = self.app.personagem
        self.combate = Combate(personagem, inimigo)

        self.log.configure(state="normal")
        self.log.delete("1.0", "end")
        self.log.configure(state="disabled")

        self.btn_continuar.pack_forget()
        self.btn_atacar.configure(state="normal")
        self.label_inimigo.configure(text=f"Combate: {inimigo.nome}")
        self._atualizar_pv()
        self._log(f"Um {inimigo.nome} bloqueia o caminho!")

    def _atualizar_pv(self):
        p, i = self.app.personagem, self.app.inimigo_atual
        self.label_pv.configure(
            text=f"{p.nome}: {p.pontos_de_vida}/{p.saude} PV      "
                 f"{i.nome}: {i.pontos_de_vida}/{i.saude} PV"
        )

    def _log(self, texto: str):
        self.log.configure(state="normal")
        self.log.insert("end", texto + "\n")
        self.log.see("end")
        self.log.configure(state="disabled")

    def atacar(self):   
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            self.combate.executar_turno()
        for linha in buffer.getvalue().splitlines():
            self._log(linha)

        self._atualizar_pv()

        personagem = self.app.personagem
        inimigo = self.app.inimigo_atual
        if not personagem.esta_vivo() or not inimigo.esta_vivo():
            self.btn_atacar.configure(state="disabled")
            self._finalizar()

    def _finalizar(self):
        personagem = self.app.personagem
        if not personagem.esta_vivo():
            self.app.mostrar_tela("TelaFim")
            return

        missao = self.app.missao_atual
        if missao.verificar_conclusao():
            buffer = io.StringIO()
            with contextlib.redirect_stdout(buffer):
                missao.conceder_recompensa(personagem)
            for linha in buffer.getvalue().splitlines():
                self._log(linha)

        self.btn_continuar.pack(pady=10)

    def continuar(self):
        hub = self.app.frames["TelaHub"]
        self.app.mostrar_tela("TelaHub")
        hub.avancar_encontro()