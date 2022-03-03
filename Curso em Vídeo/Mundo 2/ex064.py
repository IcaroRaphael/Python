"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual
foi a soma entre eles (Desconsiderando o flag).
"""
numero = soma = cont = 0
while numero != 999:
    numero = int(input("Número: "))
    if numero != 999:
        soma = soma + numero
        cont += 1
print("Foram lidos {} valores, e a soma foi de {}".format(cont, soma))
