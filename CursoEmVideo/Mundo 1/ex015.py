"""
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais
ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""
print("CALCULADORA DE ALUGUEL DE CARROS\n")
dias = int(input("Quantos dias o carro foi alugado? R: "))
distancia = float(input("Quantos KM o carro rodou? R: "))
total = (dias * 60) + (0.15 * distancia)
print("Total a pagar: R${:.2f}".format(total))
