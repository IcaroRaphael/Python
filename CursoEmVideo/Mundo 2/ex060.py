"""
Faça um programa que leia um número qualquer e mostre o seu fatorial.
"""
print("CALCULADORA DE FATORIAL")
somador = 1
numero = int(input("Insira um número: "))
print("{}!:".format(numero), end="")
while numero > 0:
    if numero > 1:
        print(" {} x".format(numero), end="")
    elif numero == 1:
        print(" {}".format(numero), end="")
    somador = somador * numero
    numero = numero - 1
print(" = {}".format(somador))
