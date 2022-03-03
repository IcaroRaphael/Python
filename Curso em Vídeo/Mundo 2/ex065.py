"""
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média
entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário
se ele quer ou não continuar a digitar valores.
"""
x = "S"
cont = soma = 0
while x == "S":
    cont += 1
    numero = int(input("Número: "))
    soma = soma + numero
    if cont == 1:
        menor = numero
        maior = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
    x = str(input("Você deseja continuar [S/N]? R:")).upper().strip()
print("-=-"*15)
print("Média: {}".format(soma/cont))
print("Maior: {}".format(maior))
print("Menor: {}".format(menor))
