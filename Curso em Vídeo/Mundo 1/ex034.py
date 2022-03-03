"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

Para salários superiores a R$1250,00, calcule um aumento de 10%.

Para os inferiores ou iguais, o aumento é de 15%.
"""
salario = float(input("Qual seu salário? R$"))

if salario > 1250:
    salario = salario + (0.1 * salario)
    print("Seu novo salário é de R${:.2f}".format(salario))
elif salario <= 1250:
    salario = salario + (0.15 * salario)
    print("Seu novo salário é de R${:.2f}".format(salario))
print("Aproveite seu aumento!")