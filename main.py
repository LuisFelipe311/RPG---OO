import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from jogador import Jogador
from personagem_jogador import PersonagemJogador, ClassePersonagem 
from inimigo import Inimigo
from item import Arma, Armadura, Pocao
from missao import Missao
from mapa import Mapa, Sala, Evento 
from jogo import Jogo
from combate import Combate 


def main():
    # Criação do mapa
    mapa = Mapa("Torre Esquecida")
    sala1 = Sala("Entrada da Torre", "Um corredor escuro e úmido.")
    sala1.adicionar_evento(Evento("armadilha", "Uma flecha dispara da parede!"))
    mapa.adicionar_sala(sala1)

    # Criação do jogo
    jogo = Jogo(
        nome="Crônicas de Aetherion",
        cenario="O reino medieval de Aetherion",
        historia="Malachar, o Feiticeiro Sombrio, despertou e ameaça o reino.",
        objetivo_principal="Derrotar Malachar na Torre Esquecida",
        mapa=mapa,
    )
    jogo.iniciar_jogo()

    # Criação do jogador e personagem
    jogador1 = Jogador("Ana")
    heroi = PersonagemJogador(
        nome="Kael", forca=14, inteligencia=10, saude=16,
        nh_fisico=12, nh_mental=9, classe=ClassePersonagem.GUERREIRO,
    )
    jogador1.escolher_personagem(heroi)
    jogo.adicionar_jogador(jogador1)

    # Equipando itens
    espada = Arma("Espada Curta", "Uma lâmina simples, porém afiada", valor=10, dano=5)
    armadura = Armadura("Couraça de Couro", "Proteção leve", valor=8, defesa=2)
    pocao = Pocao("Poção de Cura", "Restaura vida", valor=5, cura_quantidade=6)

    heroi.inventario.adicionar_item(espada)
    heroi.inventario.adicionar_item(armadura)
    heroi.inventario.adicionar_item(pocao)
    heroi.usar_item(espada)
    heroi.usar_item(armadura)

    # Entrando na sala (pode disparar evento)
    sala1.entrar(heroi)

    # Criação de um inimigo e missão
    goblin = Inimigo(
        nome="Goblin Batedor", forca=8, inteligencia=6, saude=8,
        nh_fisico=8, nh_mental=6, tipo_inimigo="Goblin", recompensa_xp=30,
    )
    missao1 = Missao("Limpar a entrada", "Derrote o goblin que guarda a entrada.", "50 XP")
    missao1.adicionar_inimigo(goblin)
    jogo.adicionar_missao(missao1)

    # Combate
    combate = Combate(heroi, goblin)
    combate.iniciar_combate()

    # Verificação de missão e vitória/derrota
    if missao1.verificar_conclusao():
        missao1.conceder_recompensa(heroi)

    print("\nVitória geral?", jogo.verificar_vitoria())
    print("Derrota geral?", jogo.verificar_derrota())


if __name__ == "__main__":
    main()