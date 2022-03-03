"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados
em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número
no dado.

# MÉTODO 1:
from random import randint
jogadores = dict()
jogadores["Jogador1"] = randint(1, 6)
jogadores["Jogador2"] = randint(1, 6)
jogadores["Jogador3"] = randint(1, 6)
jogadores["Jogador4"] = randint(1, 6)
n = 1
for x in sorted(jogadores, key = jogadores.get, reverse=True):
    print(f"{n}º Lugar: {x} com {jogadores[x]}")
    n += 1

"""
# MÉTODO 2:
from random import randint
from time import sleep
from operator import itemgetter
jogo = {
    "Jogador1": randint(1, 6),
    "Jogador2": randint(1, 6),
    "Jogador3": randint(1, 6),
    "Jogador4": randint(1, 6)}
ranking = list()
print("Valores sorteados:")
for k, v in jogo.items():
    print(f"{k}: {v}")
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print("RANKING:")
for i, v in enumerate(ranking):
    print(f"{i+1}º Lugar: {v[0]} ({v[1]}).")
    sleep(1)
