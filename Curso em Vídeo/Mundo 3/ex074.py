"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o
maior valor que estão na tupla.

SOLUÇÃO 1:
from random import randint
tupla = ()
for x in range(0, 5):
    aleatorio = randint(1, 100)
    tupla = tupla + (aleatorio,)
    if x == 0:
        menor = maior = tupla[x]
    elif x > 0:
        if tupla[x] > maior:
            maior = tupla[x]
        elif tupla[x] < menor:
            menor = tupla[x]
print(tupla)
print(f"Maior: {maior}")
print(f"Menor: {menor}")
"""
#SOLUÇÃO 2:
from random import randint
tupla = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
print("Os valores sorteados foram: ", end="")
for x in tupla:
    print(f" {x} ", end="")
print(f"\nO maior valor sorteado foi {max(tupla)}")
print(f"O menor valor sorteado foi {min(tupla)}")
