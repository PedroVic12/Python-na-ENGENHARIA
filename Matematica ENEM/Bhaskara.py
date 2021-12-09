import math


def calcular_bhaskara():
    a = float(input("Digite o Coeficiente [A]"))
    b = float(input("Digite o Coeficiente [B]"))
    c = float(input("Digite o Coeficiente [C]"))

    delta = math.sqrt(b*b - 4*a*c)
    if delta < 0:
        print("Delta negativo!")
        print(delta)
        print("Portanto, nao existe raizes reais")

    else:
        print(f"\n O delta tem o valor de: {delta} \n ")
        raiz_1 = (-b + delta) / 2*a
        raiz_2 = (-b - delta) / 2*a
        print(f'A raiz 1 é {raiz_1}\n')
        print(f"A raiz 2 é {raiz_2} ")


calcular_bhaskara()
