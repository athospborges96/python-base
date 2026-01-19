# Algoritimos:
"""sequencia de instruções lógicas que visam obter a solução de um problema"""

# Problema: Ir a padaria e comprar pão:
# Premissa: Padaria da esquina abre fds até as 16h, semana até as 19h feriado
# até as 14h, exceto natal e ano novo que fecha.

# 1. A padaria está aberta?
    # 1.1. Se hoje é feriado E é natal OU ano novo: Não
    # 1.2. Senão, se é feriado E não é natal OU ano novo antes das 14h: Sim
    # 1.3. Senão, se é fim de semana E antes das 16h: Sim
    # 1.4. Senão, se é dia de semana E antes das 19h: Sim
    # 1.5. Senão: Não
# 2. Se a padaria estiver aberta E:
    # 2.1. Se estiver chovendo: Pegar guarda-chuvas
    # 2.2. Se estiver chovendo E calor: Pegar guarda-chuvas e garrafa de agua
    # 2.3. Se estiver chovendo E frio: Pegar guarda-chuva e blusa de frio
    # 2.4. Se não estiver chovendo E calor: Pegar garrafa de água
    # 2.5. Se não estiver chovendo E frio: Pegar blusa de frio
    # 2.6. Ir até a padaria:
        # 2.6.1. Se tem pão integral E baguete: Pedir 6 de cada
        # 2.6.2. Senão, se tem apenas pão integral OU Baguete: Pedir 12
        # 2.6.3. Senão: Pedir 6 de qualquer pão
# 3. Senão
    # 3.1 Ficar e casa e comer biscoitos

# Vamos tentar implementar esse algoritmo em como um pseudocódigo em Python:

import ir, pegar, pedir, tem, comer, ficar

# Premissas:
today = "Segunda-feira"
hora = 15
natal = False
ano_novo = False
feriado = False
chovendo = True
frio = False
calor = True
semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira"]
feriados = ["Quarta-feira"]
horario_padaria = {
    "semana": 19, 
    "fim_de_semana": 16, 
    "feriado": 14
}

# Algoritmo:
if today in feriados and (natal or ano_novo):
    padaria_aberta = False
elif today in feriados and not (natal or ano_novo) and hora < horario_padaria["feriado"]:
    padaria_aberta = True
elif today not in semana and hora < horario_padaria["fim_de_semana"]:
    padaria_aberta = True
elif today in semana and hora < horario_padaria["semana"]:
    padaria_aberta = True
else:
    padaria_aberta = False

if padaria_aberta:
    if chovendo and calor:
        pegar("guarda-chuva")
        pegar("garrafa de água")
    elif chovendo and frio:
        pegar("guarda-chuva")
        pegar("blusa de frio")
    elif chovendo:
        pegar("guarda-chuva")
    elif not chovendo and calor:
        pegar("garrafa de água")
    elif not chovendo and not calor:
        pegar("blusa de frio")
    
    ir("padaria")
    
    if tem("pão integral") and tem("baguete"):
        pedir(6, "pães integrais")
        pedir(6, "baguetes")
    elif tem("pão integral") or tem("baguete"):
        pedir(12, "qualquer um dos dois tipos")
    else:
        pedir(6, "pães disponíveis")
else:
    ficar("casa")
    comer("biscoitos")