"""
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e
que se encontram no intervalo de 1 até 500.

SOLUÇÃO 1:
soma = 0
for x in range(1, 501):
    if ((x % 2) == 1) and ((x % 3) == 0):
        soma = soma + x
        print(x)
        print("+")
print("=")
print(soma)

"""
soma = 0
for x in range(1, 501, 2):
    if (x % 3) == 0:
        soma = soma + x
        print(x)
        print("+")
print("=")
print(soma)
