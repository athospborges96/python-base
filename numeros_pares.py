#!/usr/bin/env python3
"""
Faça um programa que imprima na tela apenas os números pares entre 1 e 200.

ex
'python3 numeros_pares.py'

expectativa de saída:
2
4
6
8
...200
"""
# Solução 1: Usando list comprehension
numeros_pares = [num for num in range(1, 201) if num % 2 == 0]
for num in numeros_pares:
    print(num)
print("-" * 30)

# Solução 2: Usando loop com condição
for num in range(1, 201):
    if num % 2 != 0:
        continue
    print(num)
print("-" * 30)

# Solução 3: Usando range com passo de 2
for num in range(2, 201, 2):
    print(num)
print("-" * 30)