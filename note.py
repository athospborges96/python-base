#!/usr/bin/env python3
""" Bloco de notas

Esse script funciona como um bloco de notas interativo, onde diretamente no
terminal, você consegue realizar anotações importantes, separando o conteúdo por
tópicos.

Uso: 

$ note.py new "Minha nota"
tag: tecnologia
texto: Anotação geral sobre progresso na carreira em engenharia de dados

$ note.py read tech
...
...
...

As anotações serão salvas em 'notas.txt'
"""
__version__ = "0.1.0"
__author__ = "Athos Matheus"
__license__ = "Unlicensed"

import os
import sys

cmds = ("read", "new")
path = os.curdir
filepath = os.path.join(path, "notas.txt")
        
arguments = sys.argv[1:]
if not arguments:
    print("invalid usage")
    print("Você precisa informar o modo")
    print(f"Modos disponíveis: {cmds}")
    sys.exit(1)
    
if arguments[0] not in cmds:
    print("invalid command {arguments[0]}")

if arguments[0] == "read":
    #Leitura das notas
    if len(arguments) < 2:
        print(open(filepath).read())
        print("-" * 40)
        print()
        sys.exit()
    for line in open(filepath):
        titulo, tag, texto = line.split("\t")
        if tag.lower() == arguments[1].lower():
            print(f"titulo: {titulo}")
            print(f"texto: {texto}")
            print("-" * 40)
            print()
        
if arguments[0] == "new":
    try:
        titulo = arguments[1]
    except IndexError:
        titulo = input("Qual é o titulo:").strip().title()
        
    text = [
        f"{titulo}",
        input("tag:").strip(),
        input("text:\n").strip(),
    ]
    
    with open(filepath, "a") as file_:
        file_.write("\t".join(text) + "\n")
