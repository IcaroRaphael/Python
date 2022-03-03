"""
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo entre eles.

SOLUÇÃO 1:
from time import sleep
start = 10
for x in range(0, 11):
    print(start)
    start = start - 1
    sleep(1)
print("FELIZ ANO NOVO!")
"""
#SOLUÇÃO 2:
from time import sleep
for x in range(10, 0, -1):
    print(x)
    sleep(1)
print("FELIZ ANO NOVO!")
