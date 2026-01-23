#!/usr/bin/env python3
"""
Alerta de temperatura

Faça um script que pergunta ao  usuário qual a temperatura atual e o indice de
umidade do ar. Dependendo das condições, o script deverá exibir uma mensagem
de alerta e um sinal sonoro dependendo das condições climáticas:

temp acima de 45 graus: "Alerta! Temperatura extremamente alta!" + sinal sonoro
temp vezes 3 for maior ou igual a umidade: "Alerta! Condições de calor úmido!"
    + sinal sonoro
temp entre 33 e 45 graus: "Atenção! Temperatura alta!"
temp entre 20 e 33 graus: "Temperatura agradável."
temp entre 10 e 20 graus: "Atenção! Tempo esfriou!"
temp abaixo de 10 graus: "Alerta! Temperatura extremamente baixa!"
    + sinal sonoro
"""
import os
import sys
import logging
from logging import handlers

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("alerta", log_level)
fh = handlers.RotatingFileHandler(
    "alerta.log", 
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

arguments = sys.argv[1:]

if not arguments:
    try:
        temp = float(input("Qual a temperatura atual (°C)? "))
        umidade = float(input("Qual o índice de umidade do ar (%)? "))
    except ValueError as e:
        log.error("Temperatura e umidade devem ser um numero %s", str(e))
        print("Temperatura e umidade devem ser um numero", str(e))
        sys.exit(1)
elif len(arguments) != 2:
    print(" Erro de uso: alerta.py [temperatura] [umidade]")
    sys.exit(1)
else:
    try:
        temp = float(arguments[0])
        umidade = float(arguments[1])
    except ValueError as e:
        log.error("Temperatura e umidade devem ser um numero %s", str(e))
        print("Temperatura e umidade devem ser um numero", str(e))
        sys.exit(1)

arguments = [temp, umidade]

if temp >= 45:
    print("Alerta! Temperatura extremamente alta!🥵")
    print("\a")
elif temp*3 >= umidade and temp != 0:
    print("Alerta! Condições de calor úmido!😶‍🌫️")
    print("\a")
elif temp >= 33 and temp < 45:
    print("Atenção! Temperatura alta!😥")
    print("Beba agua e use protetor solar😎")
    if umidade >60:
        print("umidade do ar ok")
    else:
        print("umidade abaixo do nivel ideal")
elif temp >= 20 and temp < 33:
    print("temperatura agradável")
    if umidade >60:
        print("umidade do ar ok")
    else:
        print("umidade abaixo do nivel ideal")
elif temp >= 10 and temp < 20:
    print("Atenção! Tempo esfriou!")
    if umidade >60:
        print("umidade do ar ok")
    else:
        print("umidade abaixo do nivel ideal")
elif temp < 10:
    print("Alerta! Temperatura extremamente baixa!🥶")
    print("\a")
    if umidade >60:
        print("umidade do ar ok")
    else:
        print("umidade abaixo do nivel ideal")
