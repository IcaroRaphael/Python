"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""
from random import randint
from time import sleep
primário = list()
secundário = list()
jogos = int(input("Quantos jogos você quer que eu sorteie? R:"))
for jogo in range(0, jogos):
    x = 0
    while x < 6:
        aleatório = randint(1, 60)
        if x == 0:
            secundário.append(aleatório)
            x += 1
        elif aleatório not in secundário:
            secundário.append(aleatório)
            x += 1
    secundário.sort()
    primário.append(secundário[:])
    secundário.clear()
for p in range(0, len(primário)):
    sleep(0.5)
    print(f"{p+1}º jogo: {primário[p]}")
