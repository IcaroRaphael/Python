"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
"""
saldo = float(input("Quantos R$ você possui? R:"))
dolares = saldo / 3.27
print("Valor convertido de R$ para US$: {:.2f}".format(dolares))
print("Você pode comprar {:.2f} dólar(es).".format(dolares))
