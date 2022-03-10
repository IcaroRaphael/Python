"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""
lista = list()
cont = 0
while True:
    escolha = ""
    lista.append(int(input("Insira um número: ")))
    cont += 1
    while (escolha != "S") and (escolha != "N"):
        escolha = str(input("Você deseja continuar[S/N]? R:")).strip().upper()
    if escolha == "N":
        print("-=-"*20)
        break
    print("-=-"*20)
#A) Quantos números foram digitados.
print(f"Foram digitados {cont} números.")
#B) A lista de valores, ordenada de forma decrescente.
lista.sort(reverse=True)
print(f"A lista dos valores em ordem decrescente: {lista}")
#C) Se o valor 5 foi digitado e está ou não na lista.
if 5 in lista:
    print("O número 5 está na lista.")
else:
    print("O número 5 não está na lista.")