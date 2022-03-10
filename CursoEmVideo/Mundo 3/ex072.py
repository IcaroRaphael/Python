"""
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""
NumExtenso = ('Zero' ,'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
               'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input("Digite um número entre 0 e 20: "))
    if num >= 0 and num <= 20:
        break
print(f"Você digitou o número '{NumExtenso[num]}'")
