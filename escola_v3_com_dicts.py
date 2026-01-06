#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
e que frequenta cada uma das atividades.
"""
__version__ = "0.1.2"

# Dados
salas = {
    "sala1": {"Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"},
    "sala2": {"Joao", "Antonio", "Carlos", "Maria", "Isolda"},
}

atividades = {
    "ingles": {"Erik", "Maia", "Joana", "Carlos", "Antonio"},
    "musica": {"Erik", "Carlos", "Maria"},
    "danca": {"Gustavo", "Sofia", "Joana", "Antonio"},
}

for nome_atividade, alunos_atividade in  atividades.items():
    print()
    print(f"Alunos da atividade {nome_atividade}\n")
    print("-" * 40)
    print()

    for nome_sala, alunos_sala in salas.items():
        alunos_inscritos = alunos_atividade & alunos_sala
        print(f"{nome_sala}: {alunos_inscritos}")
        
    print()
    print("#" * 40) 
