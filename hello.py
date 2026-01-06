#!/usr/bin/env python3
"""Hello World Multi Language.

depending on the language configured in the environment the program displays
the corresponding message.

Usage:

You need to have the LANG variable properly configured ex:

    export LANG=pt_BR

Execute:

    python3 hello.py
    or
    ./hello.py
"""
__version__ ="0.1.2"
__author__ ="Athos Matheus"
__license__ ="Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

#tanto os sets quanto os dicts implementam (Hash Table) 
#- O(1) - constante.

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde",
}

print(msg[current_language])
