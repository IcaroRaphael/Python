"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas
- O nome com todas minúsculas
- Quantas letras ao todo (sem considerar espaços)
- Quantas letras tem o primeiro nome
"""
nome = input("Nome completo: ")
print("Maiúsculas: {}".format(nome.upper()))
print("Minúsculas: {}".format(nome.lower()))
print("Total de Letras: {}".format(len(nome.replace(" ", ""))))
print("Total de letras no primeiro nome: {}".format(len(nome.split()[0])))
