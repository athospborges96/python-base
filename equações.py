import math

def resolver_equacao_2grau():
    print("Calculadora de equação do 2º Grau (ax² + bx + c = 0)")
    try:
        a = float(input("digite o coeficiente a: "))
        b = float(input("digite o coeficiente b: "))
        c = float(input("digite o coeficiente c: "))

        if a == 0:
            print("Coeficiente 'a' não pode ser zero em uma equação de 2º grau.")
            return

        delta = (b**2) - (4 * a * c)

        if delta >= 0:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)

            if delta == 0:
                print (f"A equação tem uma raiz dupla: x = {x1:.2f}")
            else:
                print (f"As raízes são: x1 = {x1:.2f} e x2 = {x2:.2f}")
        else:
            print("O discriminante é negativo. A equação não possui raízes reais.")            

    except ValueError:
        print("entrada inválida. Por favor, digite apenas números.")

resolver_equacao_2grau()

