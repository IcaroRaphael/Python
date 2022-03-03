"""
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas;
B) A média de idade do grupo;
C) Uma lista com todas as mulheres;
D) Uma lista com todas as pessoas com idade acima da média.
"""
dados = list()
cadastro = dict()
while True:
    cadastro["Nome"] = str(input('Nome: ')).title().strip()
    while True:
        cadastro["Sexo"] = str(input('Sexo[M/F]: ')).upper().strip()
        if (cadastro["Sexo"] == "M") or (cadastro["Sexo"] == "F"):
            break
        print("ERRO! Por favor, digite apenas M ou F.")
    cadastro["Idade"] = int(input("Idade: "))
    dados.append(cadastro.copy())
    while True:
        stop = str(input("Você deseja realizar um novo cadastro? [S/N]: ")).upper().strip()
        if (stop == "N") or (stop == "S"):
            break
        print("ERRO! Responda apenas S ou N.")
    if stop == "N":
        print("-=-"*20)
        break
    cadastro.clear()
    print("-=-" * 20)
# A) Quantas pessoas foram cadastradas;
print(f"A) Quantas pessoas foram cadastradas? R:{len(dados)}")
# B) A média de idade do grupo;
soma = 0
for i in range(0, len(dados)):
    soma += dados[i]["Idade"]
média = soma/len(dados)
print(f"B) A média de idade do grupo: {média}")
# C) Uma lista com todas as mulheres;
mulheres = list()
for m in range(0, len(dados)):
    if dados[m]["Sexo"] == "F":
        mulheres.append(dados[m]["Nome"])
print("C) Uma lista com todas as mulheres:")
for m in mulheres:
    print(f"- {m}")
# D) Uma lista com todas as pessoas com idade acima da média.
print("D) Uma lista com todas as pessoas com idade acima da média:")
for p in range(0, len(dados)):
    if dados[p]["Idade"] > média:
        print(f"- {dados[p]['Nome']} ({dados[p]['Idade']} anos)")
