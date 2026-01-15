#!/usr/bin/env python3
"""Hello World Multi Language.

depending on the language configured in the environment the program displays
the corresponding message.

Usage:

You need to have the LANG variable properly configured ex:

    export LANG=pt_BR

Or specify it through the CLI argument `--lang`

Or the user will have to type it.

Execute:

    python3 hello.py
    or
    ./hello.py
"""
__version__ ="0.1.3"
__author__ ="Athos Matheus"
__license__ ="Unlicense"

import os
import sys
import logging

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("hello.py", log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
fmt = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - " \
    "l:%(lineno)d - f:%(filename)s: %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S"
)
ch.setFormatter(fmt)
log.addHandler(ch)

arguments = {"lang": None, "count": 1}

for arg in sys.argv[1:]:
    try:
        key, value = arg.split("=")
    except ValueError as e:
        log.error(
            "you need to use `=` on the argument instead (%s), try " \
            "--key=value: %s",
            arg[6:7],
            str(e)
        )
        sys.exit(1)
        
    key = key.lstrip("-").strip()
    value = value.strip()

    # Validação
    if key not in arguments:
        print(f"Invalid Option`{key}`")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    #TODO: Usar repetição
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language:")

current_language = current_language[:5]

#tanto os sets quanto os dicts implementam (Hash Table) - O(1) - constante.
msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_ES": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde",
}

"""
# try com valor default
message = msg.get(current_language, msg["en_US"])
"""

try:
    message = msg[current_language]
except KeyError as e:
    log.error("Invalid Language: %s", str(e))
    print(f"Chose from:{list(msg.keys())}")
    sys.exit(1)

print(
    message * int(arguments["count"])
)
