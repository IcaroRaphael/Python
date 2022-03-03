"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
a soma entre todos os valores PARES sorteados pela função anterior.
"""
from random import randint


def sorteia(lista):
    print("Sorteando 5 valores da lista: ", end="")
    for x in range(0, 5):
        lista.append(randint(1, 10))
        print(f"{lista[x]} ", end="")
    print("PRONTO!")


def somaPar(lista):
    print(f"Somando os valores pares de {lista}, temos ", end="")
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f"{soma}.")


números = list()
sorteia(números)
somaPar(números)
