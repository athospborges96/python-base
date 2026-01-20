#!/usr/bin/env python3

#for loop

#programação estruturada/imperativa

original = [1, 2, 3, 4, 5]
dobrada = []
for n in original:
    dobrada.append(n * 2)
print(dobrada)

# Programação funcional
# List Comprehension
dobrada = [n * 2 for n in original]
print(dobrada)

# Dict comprehension
dados = {
    line.split(":")[0]: line.split(":")[1].strip() 
    for line in open("input.txt") 
    if ":" in line
}
print(dados)