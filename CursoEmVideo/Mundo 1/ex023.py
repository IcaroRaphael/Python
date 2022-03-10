"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Ex:
Digite um número: 1834
Unidade: 4
Dezena: 3
Centena: 8
Milhar: 1
"""
numero = input("Insira um número: ")
digitos = len(numero)
if digitos == 4:
    print("Unidade: {}".format(numero[3]))
    print("Dezena: {}".format(numero[2]))
    print("Centena: {}".format(numero[1]))
    print("Milhar: {}".format(numero[0]))
elif digitos == 3:
    print("Unidade: {}".format(numero[2]))
    print("Dezena: {}".format(numero[1]))
    print("Centena: {}".format(numero[0]))
elif digitos == 2:
    print("Unidade: {}".format(numero[1]))
    print("Dezena: {}".format(numero[0]))
elif digitos == 1:
    print("Unidade: {}".format(numero[0]))
