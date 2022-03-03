"""
Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando o laço for.
"""
from time import sleep
numero = int(input("Número: "))
for x in range(1, 11):
    sleep(0.2)
    print("{} x {} = {}".format(numero, x, numero*x))
