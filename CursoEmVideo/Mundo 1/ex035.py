"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
se elas podem ou não formar um triângulo
"""
r1 = float(input("1º reta: "))
r2 = float(input("2º reta: "))
r3 = float(input("3º reta: "))

if (r1 > r2) and (r1 > r3) and (r2 + r3) > r1:
    print("As retas podem formar um triângulo.")
elif (r2 > r1) and (r2 > r3) and (r1 + r3) > r2:
    print("As retas podem formar um triângulo.")
elif (r3 > r1) and (r3 > r2) and (r1 + r2) > r3:
    print("As retas podem formar um triângulo.")
else:
    print("As retas não podem formar um triângulo.")
