email_tmpl = """
Olá, %(nome)s.

Vi que seu perfil atende os requisitos para o upgrade de cartão.

Seu cartão atual é o %(cartao_basico)s.

A nossa oferta é o upgrade para o cartão %(cartao_novo)s

Com ele, você terá os benefícios:  %(pontos).1f pontos  por dólar gasto, acesso a sala vip  %(sala_vip)i vezes por ano, seguro viagem, e muito mais.

E ainda te oferecemos anuidade grátis por %(anos)d anos.

%(texto)s

cique agora em %(link)s

Oferta por tempo limitado a %(tempo)d horas.
 """

clientes = ["Athos", "Luiza", "Roberto"]

for cliente in clientes:
        print(email_tmpl % {"nome": cliente, "cartao_basico": "platinum", "cartao_novo": "grafeno plus", "pontos": 4.5, "sala_vip": 20,
        "anos": 2, "texto": "Esse é um produto exclusivo do nosso banco", "link": "https://bancodobostil.com", "tempo": 24})
