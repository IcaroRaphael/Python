"""
Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
"""
começo = float(input("Primeiro termo: "))
razão = int(input("Razão: "))
x = 1
fim = 10
while x <= fim:
    if x < fim:
        print("{}  ".format(começo), end="")
        começo = começo + razão
        x += 1
    elif x == fim:
        print("{}  ".format(começo))
        começo = começo + razão
        x += 1
        add = int(input("Você deseja ver mais quantos termos? R:"))
        fim += add
print("Fim!")
