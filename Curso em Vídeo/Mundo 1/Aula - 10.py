"""
tempo = int(input("Quantos anos tem seu carro? R:"))
if tempo <= 3:
    print("Carro novo!")
else:
    print("Carro velho!")
print("Fim")

#OU

tempo = int(input("Quantos anos tem seu carro? R:))
print("Carro novo!" if tempo <= 3 else "Carro velho")
print("Fim")
----------------------------------------------------------------------------
nome = str(input("Qual é o seu nome? R:"))
if nome == "Gustavo":
    print("Que nome lindo você tem!")
else:
    print("Seu nome é tão normal.")
print("Bom dia, {}!".format(nome))

"""
nota1 = float(input("Insira a 1º nota: "))
nota2 = float(input("Insira a 2º nota: "))
media = (nota1 + nota2)/2
print("A sua média foi {:.1f}".format(media))
if media >= 6.0:
    print("Sua média foi boa! PARABÉNS!")
else:
    print("Sua média foi ruim! ESTUDE MAIS!")
