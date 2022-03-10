"""
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.
"""
def área(l, c):
    a = l * c
    print("-=-"*15)
    print(f"Largura: {l}")
    print(f"Comprimento: {c}")
    print(f"Área: {a}")


largura = float(input("Insira a largura: "))
comprimento = float(input("Insira o comprimento: "))
área(l=largura, c=comprimento)
