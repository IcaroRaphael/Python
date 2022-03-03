"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o
usuário tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela nse o usuário venceu ou perdeu.
"""
from random import randint
escolhido = int(input("Insira seu número: "))
gerador = randint(0, 5)

if escolhido == gerador:
    print("O número escolhido foi {}. Parabéns, você venceu!".format(gerador))
else:
    print("O número escolhido foi {}. Que triste, você perdeu!".format(gerador))
print("Fim do jogo.")
