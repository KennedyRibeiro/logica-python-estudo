import math

numero = float(input("Digite o número desejado: "))

if numero > 0:
    raiz = math.sqrt(numero)
    print("A raiz do número é: ", raiz)
else:
    quadrado = numero ** 2
    print("Número ao quadrado é: ", quadrado)