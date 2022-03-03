"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar
o VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo
será negado.
"""
imóvel = float(input("Imóvel: "))
salário = float(input("Salário: "))
tempo = int(input("Tempo(Anos): "))
prestação = imóvel / (tempo * 12)
print("-" *30)
if prestação <= (salário * (30/100)):
    print("Prestações: {:.2f}".format(prestação))
    print("Empréstimo Aprovado!")
else:
    print("Prestações: {:.2f}".format(prestação))
    print("Empréstimo negado!")
