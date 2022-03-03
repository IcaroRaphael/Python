"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""
tupla = ()
cont1= cont2 = 0
for x in range(0, 4):
    num = int(input("Insira um valor: "))
    tupla = tupla + (num,)
print(f"Quantas vezes apareceu o valor 9? R:{tupla.count(9)}")
for y in tupla:
    if y == 3:
        print(f"Em que posição foi digitado o primeiro valor 3? R:{tupla.index(3)+1}")
        cont2 += 1
if cont2 == 0:
    print("O valor 3 não foi digitado nenhuma vez.")
print("Quais foram os números pares? R:", end="")
for c in tupla:
    if (c % 2) == 0:
        print(f" {c} ", end="")
        cont1 += 1
if cont1 == 0:
        print("Nenhum número par foi inserido.")
