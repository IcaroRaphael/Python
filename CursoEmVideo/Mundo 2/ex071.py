"""
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será
o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""
print("="*24, "BANCO CEV", "="*25)
while True:
    resto = dinheiro = 0
    stop = " "
    saque = int(input("Qual valor você deseja sacar? R$"))
    if saque >= 50:
        dinheiro = saque // 50
        resto = (saque % 50)
        print(f"Cédulas de R$50: {dinheiro}")
    if resto >= 20:
        dinheiro = resto // 20
        resto = (resto % 20)
        print(f"Cédulas de R$20: {dinheiro}")
    if resto >= 10:
        dinheiro = resto // 10
        resto = (resto % 10)
        print(f"Cédulas de R$10: {dinheiro}")
    if resto >= 1:
        dinheiro = resto // 1
        print(f"Cédulas de R$1: {dinheiro}")
    while (stop != "S") and (stop != "N"):
        stop = str(input("Você deseja realizar outro saque[S/N]? R:")).upper().strip()
    if stop == "N":
        break
    print("-=-"*20)
