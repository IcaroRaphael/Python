"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços.
"""
f = str(input("Frase: "))
frase = f.lower().replace(" ", "")
total = len(frase)
contador = 0
for x in range(0, total):
    if frase[x] == frase[-x-1]:
        contador = contador + 1
if contador == total:
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo!")
