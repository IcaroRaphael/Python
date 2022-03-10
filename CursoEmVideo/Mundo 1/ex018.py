"""
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""
from math import radians, sin, cos, tan
angulo = float(input("Insira o ângulo: "))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))
print("Seno: {:.3f}".format(sen))
print("Cosseno: {:.3f}".format(cos))
print("Tangente: {:.3f}".format(tan))
