"""
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

SOLUÇÃO 1:
peso = float(input("Peso: "))
maior = peso
menor = peso
for x in range(1, 5):
    peso = float(input("Peso: "))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print("Maior peso: {:.1f}kg".format(maior))
print("Menor peso: {:.1f}kg".format(menor))
"""
menor = 0
maior = 0
for x in range(1, 6):
    peso = float(input("Peso: "))
    if x == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print("Maior peso: {:.1f}kg".format(maior))
print("Menor peso: {:.1f}kg".format(menor))
