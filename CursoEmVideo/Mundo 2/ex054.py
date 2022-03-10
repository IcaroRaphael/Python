"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas
pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""
from datetime import date
maior = 0
menor = 0
for x in range(0, 7):
    atual = date.today().year
    nascimento = int(input("Ano de nascimento: "))
    idade = atual - nascimento
    if idade >= 21:
        maior = maior + 1
    elif idade < 21:
        menor = menor + 1
print("Maior idade: {}".format(maior))
print("Menor idade: {}".format(menor))
