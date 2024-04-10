
print("--------------------------------------------------")
print("  Bem-Vindo a sorveteria e Lanchonete do Kennedy  ")
print("--------------------Cardápio----------------------")
print("------| Tamanho | Cupuaçu (CP) | Açaí (AC) |------")
print("------|    P    |   R$ 10,00   | R$ 12,00  |------")
print("------|    M    |   R$ 15,00   | R$ 17,00  |------")
print("------|    G    |   R$ 19,00   | R$ 21,00  |------")
print("--------------------------------------------------")

sabor = input("Escolha o sabor desejado (CP|AC):")
tamanho = input("Escolha o tamanho desejado (P|M|G:)")

if sabor == "CP" and tamanho == "P":
    print("Você pediu Cupuaçu P, o pedido fica em: R$ 10,00")
    valor = 10
elif sabor == "CP" and tamanho == "M":
    print("Você pediu Cupuaçu M, o pedido fica em: R$ 15,00")
    valor = 15
elif sabor == "CP" and tamanho == "G":
    print("Você pediu Cupuaçu G, o pedido fica em: R$ 19,00")
    valor = 19
elif sabor == "AC" and tamanho == "P":
    print("Você pediu Açaí P, o pedido fica em: R$ 12,00")
    valor = 12
elif sabor == "AC" and tamanho == "M":
    print("Você pediu Açaí M, o pedido fica em: R$ 17,00")
    valor = 17
elif sabor == "AC" and tamanho == "G":
    print("Você pediu Açaí G, o pedido fica em: R$ 21,00")
    valor = 21
elif sabor != "CP" and sabor != "AC":
    print("Sabor Invalido. Tente novamente")
elif tamanho != "P" and tamanho != "M" and tamanho != "G":
    print("Tamanho inválido. Tente novamente")

