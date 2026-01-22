#!/usr/bin/env python3
"""
Repete vogais

Faça um programa que pede ao usuário que digite uma ou mais palavras e imprime
cada uma das palavras com suas vogais duplicadas.

ex:
python3 repete_vogal.py
'Digite uma palavra(ou enter para sair)': Athos
'Digite uma palavra(ou enter para sair)': Python
'Digite uma palavra(ou enter para sair)': <enter>
AAthoos
Pythoon
"""
words = []
vogais = [
    "A", "E", "I", "O", "U",
    "a", "e", "i", "o", "u",
    "à", "â", "á", "ã",
    "é", "è", "ê",
    "í", "ì", "î",
    "ó", "ò", "ô", "õ",
    "ú","ù","û"
]

while True:
    word = input("Digite uma palavra (ou aperte enter para sair): ").strip()
    if not word:
        break

    final_word = ""
    for letter in word:
            if letter in vogais:
                final_word += letter * 2
            else:
                final_word += letter
            # if ternário alternativo    
            # final_word = letter * 2 if letter in vogais else letter
    words.append(final_word)

print(*words, sep="\n")