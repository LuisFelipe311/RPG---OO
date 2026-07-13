# Crônicas de Aetherion — Projeto RPG (Orientação a Objetos)

Projeto acadêmico de um jogo de RPG em texto, desenvolvido para a disciplina de Orientação a Objetos. O jogo é modelado e implementado em níveis, cada um representando uma etapa de entrega do curso.

## 📖 Sobre o jogo

**Crônicas de Aetherion** se passa no reino medieval de Aetherion, ameaçado pelo retorno do Feiticeiro Sombrio Malachar. Um grupo de aventureiros — Guerreiros, Magos e Ladinos — deve reunir os Fragmentos do Selo e derrotá-lo na Torre Esquecida antes que recupere todo o seu poder.

O sistema de jogo usa testes de habilidade com **3 dados de 6 faces**: a soma dos dados deve ser **menor** que o Nível de Habilidade (Físico ou Mental) do personagem para a ação ser bem-sucedida.

Descrição completa do jogo: [`docs/Nivel1_Descricao_e_UML.md`](docs/Nivel1_Descricao_e_UML.md)

## 🗂️ Estrutura do repositório

```
.
├── docs/
│   ├── Nivel1_Descricao_e_UML.md   # Descrição do jogo + diagrama UML
│   ├── diagrama_uml_rpg.png        # Diagrama de classes (imagem)
│   ├── diagrama_uml_rpg.mmd        # Diagrama de classes (código-fonte Mermaid)
│   └── Roteiro_Video_Nivel1.md     # Roteiro do vídeo de apresentação
├── src/
│   ├── dado.py
│   ├── personagem.py
│   ├── personagem_jogador.py
│   ├── inimigo.py
│   ├── teste_habilidade.py
│   ├── item.py
│   ├── inventario.py
│   ├── jogador.py
│   ├── missao.py
│   ├── mapa.py
│   ├── combate.py
│   └── jogo.py
├── main.py                         # Script de demonstração
└── README.md
```

## 🧩 Diagrama de Classes

![Diagrama UML](docs/diagrama_uml_rpg.png)

O diagrama completo (editável) está em [`docs/diagrama_uml_rpg.mmd`](docs/diagrama_uml_rpg.mmd) e pode ser aberto em [mermaid.live](https://mermaid.live) ou com a extensão Mermaid do VSCode.

## ▶️ Como rodar

Requer Python 3.10+.

```bash
git clone <url-do-repositorio>
cd RPG---OO
python main.py
```

O `main.py` roda um cenário de demonstração: cria um personagem, equipa itens, entra em uma sala, ativa um combate contra um inimigo e verifica condições de vitória/derrota.

## 📦 Níveis do projeto

| Nível | Status | Entrega | Vídeo |
|---|---|---|---|
| Nível 1 | ✅ Concluído | Modelagem UML + descrição do jogo | *(link do YouTube aqui)* |
| Nível 2 | ⏳ Planejado | — | — |

Cada nível é versionado em uma branch própria (`nivel-1`, `nivel-2`, ...) e mergeado na `main` ao ser concluído.

