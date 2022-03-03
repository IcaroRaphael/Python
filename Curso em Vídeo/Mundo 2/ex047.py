"""
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50

SOLUÇÃO 1:
from time import sleep
print("Os números pares entre 1 e 50 são...")
for x in range(1, 51):
    if (x % 2) == 0:
        sleep(0.5)
        print(x)
"""
#SOLUÇÃO 2:
for x in range(2, 50, 2):
    print(x)
