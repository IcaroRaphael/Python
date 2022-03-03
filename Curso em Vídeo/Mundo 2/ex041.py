"""
A confederação nacional de natação precisa e um programa que leia o ano de nascimento de um atleta
e mostre sua categoria, de acordo com a idade:
- Até 9 anos: Mirim
- Até 14 anos: Infantil
- Até 19 anos: Junior
- Até 20 anos: Sênior
- Acima: Master
"""
from datetime import date
atual = date.today().year
nascimento = int(input("Ano de Nascimento: "))
idade = atual - nascimento

if idade <= 9:
    print("Idade: {}".format(idade))
    print("Categoria: Mirim")
elif idade > 9 and idade <= 14:
    print("Idade: {}".format(idade))
    print("Categoria: Infantil")
elif idade > 14 and idade <= 19:
    print("Idade: {}".format(idade))
    print("Categoria: Junior")
elif idade == 20:
    print("Idade: {}".format(idade))
    print("Categoria: Sênior")
elif idade > 20:
    print("Idade: {}".format(idade))
    print("Categoria: Master")
