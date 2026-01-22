#!/usr/bin/env python3
import os
import sys
import logging
from logging import handlers

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("errors.py", log_level)
fh = handlers.RotatingFileHandler(
    "errors.log",
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

# EAFP - Easy to Ask Forgiveness than Permission
# (É mais fácil pedir perdão do que permissão)

try: 
    names = open("names.txt").readlines() # FileNotFoundError
except FileNotFoundError as e:
    log.critical("Arquivo de nomes não encontrado: %s", str(e))
    print("arquivo de nomes não encontrado")
    sys.exit(1)
    # TODO: Usar retry
else:
    print("success!")
    print("Buscando nome...")
finally:
    print("Operação de busca finalizada.")
    
try:
    print(names[2])
except IndexError as e:
    log.error("não há nome na posição solicitada: %s", str(e))
    print("nome não encontrado")
    sys.exit(1)
 
