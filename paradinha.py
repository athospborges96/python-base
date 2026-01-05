#!/usr/bin/env python3
"""Imprime a tabuada de 1 ao 10.

-----Tabuada do 1-----

      1 x 1 = 1
      2 x 1 = 2
      3 x 1 = 3
...
########################
-----Tabuada do 2-----

      2 x 1 = 2
      2 x 2 = 4
...
########################
"""
__version__ = "0.1.1"
__author__ = "Athos"

# numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Iterable (percorriveis)
numeros = list(range (1, 11))

for n1 in numeros:
    print ("{:-^30}".format(f"Tabuada do {n1}\N{abacus}"))
    print()
    for n2 in numeros:
        resultado_mul = n1 * n2
        print("{:^30}".format(f"{n1} x {n2} = {resultado_mul}"))
    print()
    print("#" * 31)
    print()
    
print("_" * 31)
print()

numeros_divisiveis = list(range(1, 101))
for n1 in numeros_divisiveis:
    if not n1 <= 10:
        continue
    print ("{:-^30}".format(f"divisão do {n1}\N{abacus}"))
    print()
    for n2 in numeros_divisiveis:
        if n2 < n1:
            continue
        resultado_div = n2 / n1
        if not resultado_div.is_integer():
            continue
        print ("{:^30}".format(f"{n2} / {n1} = {resultado_div:.0f}"))
    print()
    print("#" * 31)
    print()
