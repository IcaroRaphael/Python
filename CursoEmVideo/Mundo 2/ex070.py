"""
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se
o usuário vai continuar. No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
C) Qual é o nome do produto mais barato.
"""
total = cont1 = 0
cont2 = 1
while True:
    print("-=-"*15)
    stop = " "
    nome = str(input("Nome: ")).upper().strip()
    preço = float(input("Preço: R$"))
    #A) Qual é o total gasto na compra.
    total += preço
    #B) Quantos produtos custam mais de R$1000.
    if preço >= 1000:
        cont1 += 1
    #C) Qual é o nome do produto mais barato.
    if cont2 == 1:
        PreçoMenor = preço
        ProdutoMenor = nome
        cont2 += 1
    else:
        if preço < PreçoMenor:
            PreçoMenor = preço
            ProdutoMenor = nome
#--------------------------------------------------
    while (stop != "S") and (stop != "N"):
        stop = str(input("Você deseja continuar [S/N]: ")).upper().strip()
    if stop == "N":
        break
print("-=-"*15)
print("Custo total: R${:.2f}".format(total))
print(f"Quantos produtos que custam mais de R$1000: {cont1}")
print(f"Qual é o nome do produto mais barato: {ProdutoMenor}(R${PreçoMenor})")
