"""
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""
cadastro = list()
pessoas = list()
pesos = list()
while True:
    stop = ""
    for x in range(0, 2):
        if x == 0:
            nome = str(input("Nome: ")).title().strip()
            cadastro.append(nome)
        elif x == 1:
            peso = float(input("Peso: "))
            cadastro.append(peso)
    pessoas.append(cadastro[:])
    cadastro.clear()
    while (stop != "S") and (stop != "N"):
        stop = str(input("Você deseja continuar? [S/N]: ")).upper().strip()
    if stop == "N":
        break
# A) Quantas pessoas foram cadastradas.
print(f"A) Quantas pessoas foram cadastradas? R: {len(pessoas)}")
# Definindo uma lista com pesos em ordem crescente.
for p in range(0, len(pessoas)):
    pesos.append(pessoas[p][1])
    pesos.sort()
# B) Uma listagem com as pessoas mais pesadas.
print("B) Uma listagem com as pessoas mais pesadas: ",)
for p in range(0, len(pessoas)):
    if pessoas[p][1] == pesos[-1]:
        print(f"- {pessoas[p][0]}, {pesos[-1]}kg")
# C) Uma listagem com as pessoas mais leves.
print("C) Uma listagem com as pessoas mais leves: ")
for p in range(0, len(pessoas)):
    if pessoas[p][1] == pesos[0]:
        print(f"- {pessoas[p][0]}, {pesos[0]}kg")
