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
__version__ ="0.0.1"
__author__ ="Athos Matheus"
__license__ ="Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour, Monde!"

print(msg)
