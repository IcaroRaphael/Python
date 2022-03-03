"""
Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
da progressão usando a estrutura while.
"""
começo = float(input("Primeiro termo: "))
razão = int(input("Razão: "))
x = 1
while x <= 10:
    print("{}  ".format(começo), end="")
    começo += razão
    x += 1
