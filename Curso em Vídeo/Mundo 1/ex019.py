"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo
o nome deles e escrevendo o nome do escolhido.

# MÉTODO 1:
import random
print("Insira o nome dos alunos")
a1 = str(input("Aluno 1: "))
a2 = str(input("Aluno 2: "))
a3 = str(input("Aluno 3: "))
a4 = str(input("Aluno 4: "))
sorteio = random.randint(1, 4)

if(sorteio == 1):
    print("Aluno '{}' foi o sorteado!".format(a1))
elif(sorteio == 2):
    print("Aluno '{}' foi o sorteado!".format(a2))
elif(sorteio == 3):
    print("Aluno '{}' foi o sorteado!".format(a3))
elif(sorteio == 4):
    print("Aluno '{}' foi o sorteado!".format(a4))
"""
# MÉTODO 2:
import random
a1 = str(input("Primeiro aluno: "))
a2 = str(input("Segundo aluno: "))
a3 = str(input("Terceiro aluno: "))
a4 = str(input("Quarto aluno: "))
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print("Aluno escolhido: {}".format(escolhido))
