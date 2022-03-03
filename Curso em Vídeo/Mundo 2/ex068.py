"""
Faça um programa que jogue PAR OU ÍMPAR com o computador. O jogo só será interrompido quando o jogador
PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
from random import randint
print("-=-"*20)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("-=-"*20)
vitorias = 0
while True:
    escolha = " "
    numero = int(input("Digite um valor: "))
    while (escolha != "P") and (escolha != "I"):
        escolha = str(input("Par ou Ímpar [P/I}? R:")).upper().strip()
    computador = randint(0, 10)
    soma = numero + computador
    if soma % 2 == 0:
        resultado = "PAR"
    else:
        resultado = "ÍMPAR"
    print("\33[4mRESULTADO:\33[m")
    print(f"Você jogou {numero} e o computador jogou {computador}. Total de {soma} deu {resultado}")
    if (escolha == "I") and (resultado == "ÍMPAR"):
        print("\33[1;32mVOCÊ VENCEU! Continue...\33[m")
        vitorias += 1
    elif (escolha == "P") and (resultado == "PAR"):
        print("\33[1;32mVOCÊ VENCEU! Continue...\33[m")
        vitorias += 1
    elif (escolha == "I") and (resultado == "PAR"):
        print(f"\33[1;31mVOCÊ PERDEU! Você teve {vitorias} vitória(s) consecutivas.\33[m")
        print("-=-" * 20)
        break
    elif (escolha == "P") and (resultado == "ÍMPAR"):
        print(f"\33[1;31mVOCÊ PERDEU! Você teve {vitorias} vitória(s) consecutivas.\33[m")
        print("-=-" * 20)
        break
    print("-=-"*8, "NOVA RODADA", "-=-"*8)
