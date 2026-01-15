#!/usr/bin/env python3

import os
import logging
from logging import handlers

#BOILERPLATE
# TODO: usar função
# TODO: usar lib (loguru)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
# Nossa instância
log = logging.Logger("logs.py", log_level)
# level ->
# ch = logging.StreamHandler()
# ch.setLevel(log_level)
fh = handlers.RotatingFileHandler(
    "logs.log", 
    maxBytes=10**6, 
    backupCount=10
)

fh.setLevel(log_level)
# formatacao ->
fmt = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - " \
    "l:%(lineno)d - f:%(filename)s: %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S"
)
#ch.setFormatter(fmt)
fh.setFormatter(fmt)
# destino ->
#log.addHandler(ch)
log.addHandler(fh)

"""
log.debug("mensagem pro dev, qe, sysadmin")
log.info("mensagem informativa pro usuário")
log.warning("mensagem de algo que não impede o funcionamento")
log.error("algo que impede o funcionamento de uma unica execução")
log.critical("Erro geral, ex: banco de dados desapareceu")
"""

try:
    1/0
except ZeroDivisionError as e:
    log.error("Deu erro %s", str(e))
    # stdout
    # stderr