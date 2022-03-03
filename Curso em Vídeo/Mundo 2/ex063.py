"""
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos
de uma sequência de fibonacci.
numero = int(input("Insira um número: "))
"""
max = int(input("Quantos termos da sequência? R:"))
fn = 1
x = 0
print("{}  ".format(fn), end="")
while x < (max-1):
    if x == 0:
        termo1 = fn-1
        termo2 = fn
        fn = termo1 + termo2
        termo1 = termo2
        termo2 = fn
    elif x > 0:
        fn = termo1 + termo2
        termo1 = termo2
        termo2 = fn
    print("{}  ".format(fn), end="")
    x += 1
