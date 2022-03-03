"""
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados
"""
print("CALCULADORA DE TINTA")
largura = float(input("Insira a Largura: "))
altura = float(input("Insira a Altura: "))
area = largura * altura
print("Área Total: {:.2f} Metros Quadrados".format(area))
tinta = area / 2
print("Será necessário {:.2f} litros de tinta.".format(tinta))
