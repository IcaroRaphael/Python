"""
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo
e realize a contagem.

Seu programa tem que realizar três contagens através da função criada:
A) De 1 até 10, de 1 em 1
B) De 10 até 0, de 2 em 2
C) Uma contagem personalizada
"""
from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    if inicio < fim:
        while inicio <= fim:
            print(f" {inicio} ", end="")
            sleep(0.5)
            inicio += passo
        print("FIM!")
    elif inicio > fim:
        while inicio >= fim:
            print(f" {inicio} ", end="")
            sleep(0.5)
            inicio -= passo
        print("FIM!")


# A) De 1 até 10, de 1 em 1
print("-=-"*20)
print("A) De 1 até 10, de 1 em 1: ")
contador(1, 10, 1)
# B) De 10 até 0, de 2 em 2
print("-=-"*20)
print("B) De 10 até 0, de 2 em 2: ")
contador(10, 0, 2)
# C) Uma contagem personalizada
print("-=-"*20)
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
print("C) Uma contagem personalizada: ")
contador(inicio, fim, passo)
