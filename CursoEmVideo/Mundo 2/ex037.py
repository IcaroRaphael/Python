"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será
a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal
"""
print("CONVERSOR DE BASES NUMÉRICAS")
numero = int(input("Insira um número: "))
print("1 - Binário")
print("2 - Octal")
print("3 - Hexadecimal")
tipo = int(input("Você deseja converter para Binário, Octal ou Hexadecimal? R:"))

if tipo == 1:
    binário = format(numero, "b")
    print("Inteiro: {}".format(numero))
    print("Binário: {}".format(binário))
elif tipo == 2:
    octal = format(numero, "o")
    print("Inteiro: {}".format(numero))
    print("Octal: {}".format(octal))
elif tipo == 3:
    hexadecimal = format(numero, "x")
    print("Inteiro: {}".format(numero))
    print("Hexadecimal: {}".format(hexadecimal))
else:
    print("Opção Inválida.")
