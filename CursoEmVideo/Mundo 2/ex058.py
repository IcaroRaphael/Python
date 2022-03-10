"""
Melhore o jogo do DESAFIO 028 onde o computador vai "Pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
palpites foram necessários para vencer.
"""
from random import randint
from time import sleep
print("-=-"*20)
jogador = int(input("Estou pensando em qual número entre 0 e 10? R:"))
print("Calculando...")
sleep(1)
computador = randint(0, 10)
print("""Computador: {}
Jogador: {}""".format(computador, jogador))
cont = 1
print("-=-"*20)
while jogador != computador:
    print("Errou! Tente novamente.")
    jogador = int(input("Estou pensando em qual número entre 0 e 10? R:"))
    print("Calculando...")
    sleep(1)
    computador = randint(0, 10)
    print("""Computador: {}
Jogador: {}""".format(computador, jogador))
    cont += 1
    print("-=-"*20)
print("Parabéns, você venceu! Foram {} tentativas até você conseguir.".format(cont))
