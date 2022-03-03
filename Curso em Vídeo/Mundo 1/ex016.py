"""
Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
"""
"""
# MÉTODO 1: 
num = float(input("Insira um número: "))
num = num // 1
print("Parte Inteira: {:.0f}".format(num))

# MÉTODO 2:
import math
num = math.trunc(float(input("Insira um número: ")))
print("Parte Inteira: {:.0f}".format(num))
"""
# MÉTODO 3:
num = float(input("Insira um número: "))
print("Parte Inteira: {}".format(int(num)))
