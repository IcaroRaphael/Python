"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
"""
nome = input("Nome Completo: ")
nome = nome.title().split()
digitos = len(nome)
for x in range(digitos):
    if nome[x] == "Silva":
        print("O nome {} é Silva".format(x+1))
    else:
        print("O nome {} não é Silva".format(x+1))
