"""
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""
números = [[], []]
for x in range(0, 7):
    numero = int(input(f"Insira o {x+1}º número: "))
    if (numero % 2) == 0:
        números[0].append(numero)
    else:
        números[1].append(numero)
print(f"Pares: {sorted(números[0])}")
print(f"Ímpares: {sorted(números[1])}")
