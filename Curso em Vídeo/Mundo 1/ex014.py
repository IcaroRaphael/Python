"""
Escreva um programa que converta uma temperatura digitada em graus Celsius e converta para graus Fahrenheit.
"""
print("CONVERSOR DE TEMPERATURA\n")
print("Qual conversão você deseja fazer?")
print("1 - Celsius -> Fahrenheit")
print("2 - Fahrenheit -> Celsius")
print("3 - Celsius -> Kelvin")
print("4 - Kelvin -> Celsius")
print("5 - Fahrenheit -> Kelvin")
print("6 - Kelvin -> Fahrenheit")
escolha = int(input("Insira: "))
print("-"*30)

if(escolha == 1):
    c = float(input("Celsius: "))
    f = (c * 1.8) + 32
    print("Fahrenheit: {:.2f}".format(f))
elif(escolha == 2):
    f = float(input("fahrenheit: "))
    c = (f - 32) / 1.8
    print("Celsius: {:.2f}".format(c))
elif(escolha == 3):
    c = float(input("Celsius: "))
    k = c + 273.15
    print("Kelvin: {:.2f}".format(k))
elif(escolha == 4):
    k = float(input("Kelvin: "))
    c = k - 273.15
    print("Celsius: {:.2f}".format(c))
elif(escolha == 5):
    f = float(input("Fahrenheit: "))
    k = (f + 459.67) * 5/9
    print("Kelvin: {:.2f}".format(k))
elif(escolha == 6):
    k = float(input("Kelvin: "))
    f = 1.8 * (k - 273.15) + 32
    print("Fahrenheit: {:.2f}".format(f))
else:
    print("Comando Inválido.")
