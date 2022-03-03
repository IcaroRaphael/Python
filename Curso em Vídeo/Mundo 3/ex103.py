"""
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador
e quantos gols ele marcou.

O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""
def ficha(nome , gols):
    print(f"O jogador {nome} fez {gols} gols(s) no campeonato.")


nome = str(input("Nome do Jogador: "))
if nome == "":
    nome = "<desconhecido>"
gols = str(input("Número de Gols: "))
if gols == "":
    gols = 0
else:
    gols = int(gols)
ficha(nome, gols)
