#!/user/bin/env python3
"""Imprime a mensagem de um e-mail

NÃO SERVE PRA MANDAR SPAM!!!😏
"""
__version__ = "0.1.1"

import sys
import os

arguments = sys.argv[1:]
if not arguments:
    print("informe o nome do arquivo de emails")
    sys.exit(1)
    
filename =  arguments [0]

#TODO: melhorar isso aqui
if(arguments) <2:
    print("informe o arquivo de template")
    sys.exit(1)

templatename = arguments [1]

path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, templatename)


for line in open(filepath):
    name, email = line.split(",")

    # TODO:Substituir por enviar email de verdade
    print(f"Enviando email para: {email}")
    print()
    print(
        open(templatepath).read() 
        % {
            "nome": name, 
            "cartao_basico": "platinum", 
            "cartao_novo": "grafeno plus", 
            "pontos": 4.5, 
            "sala_vip": 20,
            "anos": 2, 
            "texto": "Esse é um produto exclusivo do nosso banco", 
            "link": "https://bancodobostil.com", 
            "tempo": 24,
        }
    )
    print("-" * 50)
