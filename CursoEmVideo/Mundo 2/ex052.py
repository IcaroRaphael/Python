"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""
numero = int(input("Número: "))
contador = 0
for x in range(1, numero+1):
    if (numero % x) == 0:
        contador = contador + 1
if contador == 2:
    print("Número {} é primo!".format(numero))
else:
    print("Número {} não é primo!".format(numero))
