"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""
jogador = dict()
gols = list()
jogador["Nome"] = str(input("Nome do Jogador: ")).title().strip()
partidas = int(input(f"Quantas partidas {jogador['Nome']} jogou? R:"))
total = 0
for x in range(0, partidas):
    gols.append(int(input(f"Quantos gols na partida {x+1}? R:")))
    total += gols[x]
jogador["Gols"] = gols
jogador["Total"] = total
print(f"O jogador {jogador['Nome']} jogou {partidas} partidas.")
for p in range(0, partidas):
    print(f"    => Na partida {p+1}, fez {gols[p]} gols.")
print(f"Foi um total de {total} gols.")
