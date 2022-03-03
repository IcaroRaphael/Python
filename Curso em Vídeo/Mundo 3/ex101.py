"""
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma
pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL, OBRIGATÓRIO nas eleições.
"""
from datetime import date
atual = date.today().year


def voto(nasci):
    global atual
    idade = atual - nasci
    if idade < 0:
        print("Parâmetro Inválido.")
    elif (idade > 0) and (idade < 16):
        return "NEGADO"
    elif (idade >= 16) and (idade < 18):
        return "OPCIONAL"
    elif (idade >= 18) and (idade < 70):
        return "OBRIGATÓRIO"
    elif (idade >= 70):
        return "OPCIONAL"


nascimento = int(input("Insira seu ano de nascimento: "))
print(f"Idade: {atual - nascimento}")
print(f"Situação: {voto(nascimento)}")
