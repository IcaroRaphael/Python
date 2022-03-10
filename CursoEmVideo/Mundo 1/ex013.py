"""
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""
print("CALCULADORA DE AUMENTO")
salario = float(input("Insira seu salário atual: R$"))
aumento = float(input("Insira o percentual de aumento: "))
print("Salário atual: R${:.2f}".format(salario))
print("Aumento: {:.2f}%".format(aumento))
aumento = aumento / 100
novo = salario + (salario * aumento)
print("Novo salário: R${:.2f}".format(novo))
