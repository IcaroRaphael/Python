"""
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.

Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
from time import sleep


def maior(* valores):
    maior = 0
    print("-=-"*20)
    print("Analisando os valores passados...")
    for valor in valores:
        print(f"{valor} ", end="")
        sleep(0.5)
    print(f"Foram informados {len(valores)} valores ao todo.")
    for x in range(0, len(valores)):
        if x == 0:
            maior = valores[x]
        else:
            if valores[x] > maior:
                maior = valores[x]
    print(f"O maior valor informado foi {maior}.")


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
