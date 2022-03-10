"""
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer com parâmetro e mostre
uma mensagem com tamanho adaptável.

Ex:
escreva("Olá, Mundo!")

Saída:
-----------
Olá, Mundo!
-----------
"""
def escreva(txt):
    linha = "~"*(len(txt)+4)
    print(linha)
    print(f"  {txt}  ")
    print(linha)


texto = str(input("Insira o texto:"))
escreva(texto)
