"""
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""
numero = int(input("Insira um número: "))
resultado = numero % 2

if resultado == 0 and numero != 0:
    print("O número {} é PAR.".format(numero))
elif resultado == 0 and numero == 0:
    print("O número {} é neutro.".format(numero))
else:
    print("O número {} é ÍMPAR.".format(numero))
