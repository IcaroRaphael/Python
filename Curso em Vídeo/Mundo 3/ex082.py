"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
"""
valores = list()
pares = list()
ímpares = list()
while True:
    escolha = ""
    valores.append(int(input("Insira um número: ")))
    while (escolha != "S") and (escolha != "N"):
        escolha = str(input("Você deseja continuar[S/N]? R:")).strip().upper()
    if escolha == "N":
        print("-=-"*20)
        break
    print("-=-" * 20)
for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        ímpares.append(v)
print(f"A lista completa: {valores}")
print(f"A lista dos pares: {pares}")
print(f"A lista dos ímpares: {ímpares}")
