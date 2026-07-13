"""Módulo de persistência - salva e carrega o progresso do jogo em JSON."""
from __future__ import annotations
import json
import os

from personagem_jogador import PersonagemJogador, ClassePersonagem
from item import Arma, Armadura, Pocao

CAMINHO_PADRAO = "save.json"


def _item_para_dict(item) -> dict:
    dados = {"nome": item.nome, "descricao": item.descricao, "valor": item.valor}
    if isinstance(item, Arma):
        dados["tipo"] = "Arma"
        dados["dano"] = item.dano
    elif isinstance(item, Armadura):
        dados["tipo"] = "Armadura"
        dados["defesa"] = item.defesa
    elif isinstance(item, Pocao):
        dados["tipo"] = "Pocao"
        dados["cura_quantidade"] = item.cura_quantidade
    return dados


def _item_de_dict(dados: dict):
    tipo = dados["tipo"]
    if tipo == "Arma":
        return Arma(dados["nome"], dados["descricao"], dados["valor"], dados["dano"])
    if tipo == "Armadura":
        return Armadura(dados["nome"], dados["descricao"], dados["valor"], dados["defesa"])
    if tipo == "Pocao":
        return Pocao(dados["nome"], dados["descricao"], dados["valor"], dados["cura_quantidade"])
    raise ValueError(f"Tipo de item desconhecido: {tipo}")


def personagem_para_dict(personagem: PersonagemJogador) -> dict:
    """Serializa um PersonagemJogador (e seu inventário) para um dicionário."""
    return {
        "nome": personagem.nome,
        "forca": personagem.forca,
        "inteligencia": personagem.inteligencia,
        "saude": personagem.saude,
        "nh_fisico": personagem.nh_fisico,
        "nh_mental": personagem.nh_mental,
        "pontos_de_vida": personagem.pontos_de_vida,
        "classe": personagem.classe.name,
        "experiencia": personagem.experiencia,
        "nivel": personagem.nivel,
        "inventario": [_item_para_dict(i) for i in personagem.inventario.itens],
        "arma_equipada": personagem.arma_equipada.nome if personagem.arma_equipada else None,
        "armadura_equipada": personagem.armadura_equipada.nome if personagem.armadura_equipada else None,
    }


def personagem_de_dict(dados: dict) -> PersonagemJogador:
    """Reconstrói um PersonagemJogador a partir de um dicionário salvo."""
    p = PersonagemJogador(
        nome=dados["nome"],
        forca=dados["forca"],
        inteligencia=dados["inteligencia"],
        saude=dados["saude"],
        nh_fisico=dados["nh_fisico"],
        nh_mental=dados["nh_mental"],
        classe=ClassePersonagem[dados["classe"]],
    )
    p.pontos_de_vida = dados["pontos_de_vida"]
    p.experiencia = dados["experiencia"]
    p.nivel = dados["nivel"]

    for item_dados in dados["inventario"]:
        item = _item_de_dict(item_dados)
        p.inventario.adicionar_item(item)
        if item_dados["nome"] == dados.get("arma_equipada"):
            p.arma_equipada = item
        if item_dados["nome"] == dados.get("armadura_equipada"):
            p.armadura_equipada = item

    return p


def salvar_jogo(personagem: PersonagemJogador, encontro_atual: int, caminho: str = CAMINHO_PADRAO) -> None:
    """Salva o estado completo do jogo (personagem + progresso) em um arquivo JSON."""
    dados = {
        "personagem": personagem_para_dict(personagem),
        "encontro_atual": encontro_atual,
    }
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)


def carregar_jogo(caminho: str = CAMINHO_PADRAO):
    """Carrega o jogo salvo. Retorna (personagem, encontro_atual) ou None se não existir save."""
    if not os.path.exists(caminho):
        return None
    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)
    personagem = personagem_de_dict(dados["personagem"])
    return personagem, dados["encontro_atual"]


def existe_save(caminho: str = CAMINHO_PADRAO) -> bool:
    return os.path.exists(caminho)