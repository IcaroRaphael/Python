"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo  retângulo, calcule
e mostre o comprimento da hipotenusa.
"""
from math import sqrt
print("CALCULADORA DE HIPOTENUSA")
cateto1 = float(input("Cateto 1: "))
cateto2 = float(input("Cateto 2: "))
hipotenusa = sqrt(cateto1**2 + cateto2**2)
print("Hipotenusa: {:.2f}".format(hipotenusa))
