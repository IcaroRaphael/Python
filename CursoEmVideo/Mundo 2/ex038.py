"""
Escreva um programa que leia DOIS NÚMEROS inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais.
"""
n1 = int(input("1º número: "))
n2 = int(input("2º número: "))

if n1 > n2:
    print("{} > {}".format(n1, n2))
elif n2 > n1:
    print("{} > {}".format(n2, n1))
elif n1 == n2:
    print("{} = {}".format(n1, n2))
