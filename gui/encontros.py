"""Define a sequência fixa de encontros (salas + inimigos + missões) da Torre Esquecida."""
from mapa import Sala, Evento
from inimigo import Inimigo
from missao import Missao


def criar_encontros():
    """Retorna uma lista de dicts: {sala, inimigo, missao}, na ordem em que devem ser enfrentados."""
    encontros = []

    # Encontro 1
    sala1 = Sala("Entrada da Torre", "Um corredor escuro e úmido. Ecos distantes ressoam pelas paredes.")
    sala1.adicionar_evento(Evento("armadilha", "Uma flecha dispara de um mecanismo escondido!"))
    goblin = Inimigo("Goblin Batedor", forca=8, inteligencia=6, saude=8,
                      nh_fisico=8, nh_mental=6, tipo_inimigo="Goblin", recompensa_xp=30)
    missao1 = Missao("Limpar a entrada", "Derrote o goblin que guarda a entrada.", "50 XP")
    missao1.adicionar_inimigo(goblin)
    encontros.append({"sala": sala1, "inimigo": goblin, "missao": missao1})

    # Encontro 2
    sala2 = Sala("Corredor dos Sussurros", "Vozes indistintas parecem sussurrar seu nome nas sombras.")
    sala2.adicionar_evento(Evento("cura", "Você encontra uma fonte de água abençoada."))
    bandido = Inimigo("Bandido Renegado", forca=11, inteligencia=8, saude=12,
                       nh_fisico=11, nh_mental=8, tipo_inimigo="Bandido", recompensa_xp=45)
    missao2 = Missao("Passagem livre", "Derrote o bandido que bloqueia o corredor.", "70 XP")
    missao2.adicionar_inimigo(bandido)
    encontros.append({"sala": sala2, "inimigo": bandido, "missao": missao2})

    # Encontro 3
    sala3 = Sala("Salão dos Guardiões", "Estátuas de pedra ladeiam um salão em ruínas.")
    sala3.adicionar_evento(Evento("armadilha", "O chão cede sob seus pés por um instante."))
    guardiao = Inimigo("Guardião de Pedra", forca=15, inteligencia=5, saude=18,
                        nh_fisico=14, nh_mental=6, tipo_inimigo="Guardião", recompensa_xp=80)
    missao3 = Missao("Romper a guarda", "Derrote o Guardião de Pedra.", "100 XP")
    missao3.adicionar_inimigo(guardiao)
    encontros.append({"sala": sala3, "inimigo": guardiao, "missao": missao3})

    # Encontro final
    sala4 = Sala("Topo da Torre", "Malachar aguarda, envolto em uma névoa sombria.")
    malachar = Inimigo("Malachar, o Feiticeiro Sombrio", forca=16, inteligencia=17, saude=18,
                        nh_fisico=16, nh_mental=17, tipo_inimigo="Chefe Final", recompensa_xp=200)
    missao_final = Missao("Derrotar Malachar", "Enfrente e derrote o Feiticeiro Sombrio.", "200 XP")
    missao_final.adicionar_inimigo(malachar)
    encontros.append({"sala": sala4, "inimigo": malachar, "missao": missao_final})

    return encontros