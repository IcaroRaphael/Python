"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.
"""
from time import sleep
ContIdade = ContHomens = ContMulheres = 0
while True:
    sexo = parada = " "
    print("\33[1;32m-=-"*15)
    print("CADASTRE UMA PESSOA")
    print("-=-"*15, "\33[m")
    idade = int(input("Idade: "))
    while (sexo != "M") and (sexo != "F"):
        sexo = str(input("Sexo[M/F]: ")).upper().strip()
    if idade >= 18:
        ContIdade += 1
    if sexo == "M":
        ContHomens += 1
    if (sexo == "F") and (idade < 20):
        ContMulheres += 1
    while (parada != "S") and (parada != "N"):
        parada = str(input("\33[4mVocê deseja continuar[S/N]? R:\33[m")).upper().strip()
    if parada == "N":
            break
print("\33[1;32m-=-"*15)
print("Analisando...")
sleep(1)
print("-=-"*15, "\33[m")
print(f"Pessoas com mais de 18 anos: {ContIdade}")
print(f"Homens cadastrados: {ContHomens}")
print(f"Mulheres com menos de 20 anos: {ContMulheres}")
