"""
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""
n1 = float(input("Insira o 1º número: "))
n2 = float(input("Insira o 2º número: "))
n3 = float(input("Insira o 3º número: "))

if n1 > n2 and n1 > n3:
    print("{} é o maior número.".format(n1))
elif n1 < n2 and n1 < n3:
    print("{} é o menor número.".format(n1))
if n2 > n1 and n2 > n3:
    print("{} é o maior número.".format(n2))
elif n2 < n1 and n2 < n3:
    print("{} é o menor número.".format(n2))
if n3 > n1 and n3 > n2:
    print("{} é o maior número.".format(n3))
elif n3 < n1 and n3 < n2:
    print("{} é o menor número.".format(n3))
if n1 == n2 and n1 > n3:
    print("{} é o maior número.".format(n1))
elif n1 == n2 and n1 < n3:
    print("{} é o menor número.".format(n1))
if n1 == n3 and n1 > n2:
    print("{} é o maior número.".format(n1))
elif n1 == n3 and n1 < n2:
    print("{} é o menor número.".format(n1))
if n2 == n3 and n2 > n1:
    print("{} é o maior número.".format(n2))
elif n2 == n3 and n2 < n1:
    print("{} é o menor número.".format(n2))
