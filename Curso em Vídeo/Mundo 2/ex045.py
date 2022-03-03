"""
Crie um programa que faça o computador jogar jokenpô com você.
"""
from random import randint
from time import sleep
print("** JOKENPÔ **\n")
start = int(input("Digite 1 para começar ou 2 para cancelar: "))
while start == 1:
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")
    escolha = int(input("Digite sua escolha: "))
    print("-"*40)
    aleatorio = randint(1 , 3)
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PÔ!!!")
    if (aleatorio == 1) and (escolha == 1):
        print("Pedra(Você) x Pedra(Máquina)")
        print("Empate!")
    elif (aleatorio == 1) and (escolha == 2):
        print("Papel(Você) x Pedra(Máquina)")
        print("Você ganhou!")
    elif (aleatorio == 1) and (escolha == 3):
        print("Tesoura(Você) x Pedra(Máquina)")
        print("Você perdeu!")
    elif (aleatorio == 2) and (escolha == 1):
        print("Pedra(Você) x Papel(Máquina)")
        print("Você perdeu!")
    elif (aleatorio == 2) and (escolha == 2):
        print("Papel(Você) x Papel(Máquina)")
        print("Empate!")
    elif (aleatorio == 2) and (escolha == 3):
        print("Tesoura(Você) x Papel(Máquina)")
        print("Você ganhou!")
    elif (aleatorio == 3) and (escolha == 1):
        print("Pedra(Você) x Tesoura(Máquina)")
        print("Você ganhou!")
    elif (aleatorio == 3) and (escolha == 2):
        print("Papel(Você) x Tesoura(Máquina)")
        print("Você perdeu!")
    elif (aleatorio == 3) and (escolha == 3):
        print("Tesoura(Você) x Tesoura(Máquina)")
        print("Empate!")
    print("-" * 40)
    start = int(input("Digite 1 para jogar ou 2 para cancelar: "))
