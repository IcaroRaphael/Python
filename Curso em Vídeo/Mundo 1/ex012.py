"""
Faça um algorítmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""
print("CALCULADORA DE DESCONTO")
preco = float(input("Insira o Preço: R$"))
desconto = float(input("Insira o Percentual de Desconto: "))
print("Preço: R${}".format(preco))
print("Desconto: {}%".format(desconto))
desconto = desconto / 100
novo = preco - (preco * desconto)
print("Novo Preço: R${:.2f}".format(novo))
