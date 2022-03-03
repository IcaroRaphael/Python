"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
"""
soma = 0
velho = 0
ContMulheres = 0
for x in range(1, 5):
    print("---------- {}º Pessoa ----------".format(x))
    nome = str(input("Nome: ")).title().strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo[M/F]: ")).upper().strip()
    soma = idade + soma
    if idade > velho:
        MaisVelho = nome
        velho = idade
    if (idade < 20) and (sexo == "F"):
        ContMulheres = ContMulheres + 1
print("-=-"*12)
print("Média de idade: {}".format(soma/4))
print("Nome do mais velho: {}".format(MaisVelho))
print("Mulheres menores de 20 anos: {}".format(ContMulheres))
