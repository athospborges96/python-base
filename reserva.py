#!/usr/bin/env python3
"""
Faça um programa de terminal que exibe ao usuário uma lista dos quartos
disponíveis para alugar e o preço de cada quarto, esta informação está
disponivel em um arquivo de texto separado por vírgulas.

'quartos.txt'
# codigo, nome, preço
1, Suíte Master, 500
2, Quarto Família, 350
3, Quarto single, 250
4, Quarto simples, 150

O programa pergunta ao usuário o nome completo, qual o número do quarto a ser reservado
e a quantidade de dias, e no final exibe o valor estimado a ser pago.

O programa deve salvar esta escolha em outro arquivo contendo as reservas.

'reservas.txt'
# Cliente, quarto, diarias
Bruno, 3, 12

Se outro usuário tentar reservar o mesmo quarto o programa deve exibir uma
mensagem informando que já está esgotado quartos dessa categoria.
"""

import os
import sys
import logging
from logging import handlers
from datetime import datetime

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("reserva.py", log_level)
fh = handlers.RotatingFileHandler(
    "reserva.log",
    maxBytes=10**6,
    backupCount=10
)
fh.setLevel(log_level)
fmt = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - " \
    "l:%(lineno)d - f:%(filename)s: %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S"
)
fh.setFormatter(fmt)
log.addHandler(fh)

try:
    quartos_linhas = open("quartos.txt").readlines()
except FileNotFoundError as e:
    log.critical("Lista de quartos não encontrada: %s", str(e))
    sys.exit(1)
    n
print("Hotel Ultramegablaster")
print("-" * 40)

quartos = []
for quarto in quartos_linhas:
    linha = quarto.strip()
    if not linha or linha.startswith("#"):
        continue
    codigo, nome, preco, disponiveis = [
        dado.strip() for dado in linha.split(",")
    ]
    quartos.append({
        "codigo": codigo,
        "nome": nome,
        "preco": float(preco),
        "disponiveis": int(disponiveis)
        }
    )
print("Quartos disponíveis: ")
for info in quartos:
    print(
        f"{info['codigo']} - "
        f"{info['nome']} - "
        f"R$ {info['preco']:.2f} - "
        f"({info['disponiveis']} disponiveis)"
    )
print("-" * 40)

cont = input("Quer reservar um quarto?[Y/n]: ").strip().lower()
if cont != "y":
    sys.exit(1)

print()
print("Dados para reserva")
name = input("Qual seu nome completo: ")

while True:
    codigo_quarto = input("qual o codigo do quarto: ").strip()
    quarto_escolhido = next(
        (
            info for info in quartos 
            if info['codigo'] == codigo_quarto
        )
        , None
    )
    if not quarto_escolhido:
        print("Código de quarto inválido, tente novamente")
        continue
    if quarto_escolhido["disponiveis"] <= 0:
        print("Quarto esgotado para esta categoria. Escolha outro")
        continue
    break

diarias_raw = input("Quantos dias ficará?(ex: 10): ").strip()
if not diarias_raw.isdigit():
    print(f"formato inválido {diarias_raw}")
    sys.exit(1)
diarias = int(diarias_raw)


preco_total = quarto_escolhido["preco"] * diarias
print(name, codigo_quarto, diarias, f"R$ {preco_total:.2f}")
if input("Confirma sua reserva?[Y/n]:  ").strip().lower() != "y":
    sys.exit(1)
else:
    pass
    print("Sua reserva foi confirmada")

quarto_escolhido["disponiveis"] -= 1
with open("quartos.txt", "w") as file_:
    file_.write("#codigo, nome, preço, disponiveis\n")
    for info in quartos:
        file_.write(
            f"{info['codigo']}, "
            f"{info['nome']}, "
            f"{int(info['preco'])}, "
            f"{info['disponiveis']}\n"
        )

path = os.curdir
filepath = os.path.join(path, "reservas.txt")
timestamp = datetime.now().isoformat()
user =  os.getenv('USER', 'anonymous')
try:
    with open(filepath, "a") as file_:
        file_.write(f"{timestamp[:-7]} - {name}, {codigo_quarto}, {diarias}\n")
except PermissionError as e:
    log.error("Sem permissão para escrever o arquivo %s", str(e))
    sys.exit(1)