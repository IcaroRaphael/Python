"""
ORDEM DE PRECEDÊNCIA:
1º:  ()
2º:  **
3º:  *  /  //  %
4º:  +  -
"""

# OPERADORES ARITMÉTICOS:
n1 = int(input("1º número: "))
n2 = int(input("2º número: "))
print()

#Soma:
resultado = n1 + n2
print("{} + {} = {}".format(n1, n2, resultado))

#Subtração:
resultado = n1 - n2
print("{} - {} = {}".format(n1, n2, resultado))

#Multiplicação:
resultado = n1 * n2
print("{} * {} = {}".format(n1, n2, resultado))

#Divisão:
resultado = n1 / n2
print("{} / {} = {:.2f}".format(n1, n2, resultado))

#Exponencial:
resultado = n1 ** n2
print("{} ** {} = {}".format(n1, n2, resultado))

#Divisão Inteira:
resultado = n1 // n2
print("{} // {} = {}".format(n1, n2, resultado))

#Resto de Divisão
resultado = n1 % n2
print("{} % {} = {}".format(n1, n2, resultado))

#Raíz:
resultado = n1**(1/n2)
print("Raíz {} de {} = {}".format(n2, n1, resultado))
