"""
Crie um programa que leia dois valores e mostre um menu na tela:
[1]Somar
[2]Multiplicar
[3]Maior
[4]Novos números
[5]Sair do programa
Seu programa deverá realizar a operação solicitada em casa caso.
"""
sair = 0
while sair != 1:
    print("Insira 2 valores quaisquer...")
    n1 = float(input("Valor 1: "))
    n2 = float(input("Valor 2: "))
    print("""MENU:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa""")
    menu = int(input("Opção: "))
    if menu == 1:
        print("{} + {} = {}".format(n1, n2, n1+n2))
    elif menu == 2:
        print("{} x {} = {}".format(n1, n2, n1*n2))
    elif menu == 3:
        if n1 > n2:
            print("{} > {}".format(n1, n2))
        elif n2 > n1:
            print("{} > {}".format(n2, n1))
        else:
            print("{} = {}".format(n1, n2))
    elif menu == 4:
        sair = 0
    elif menu == 5:
        sair = 1
    else:
        print("Opção inválida.")
    print("-=-"*20)
print("Fim!")
print("-=-"*20)
