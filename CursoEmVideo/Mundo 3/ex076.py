"""
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""
print("############### LISTA ###############")
listagem = ()
while True:
    stop = ""
    produto = str(input("Produto: ")).strip().upper()
    listagem = listagem + (produto,)
    preço = float(input("Preço: "))
    listagem = listagem + (preço,)
    while (stop != "S") and (stop != "N"):
        stop = str(input("Você deseja continuar[S/N]? R:")).upper().strip()
    if stop == "N":
        break
    print("-"*38)
print("############### PREÇOS ################")
for x in range(0, len(listagem)):
    if (x % 2) == 0:
        print(f"{listagem[x]:.<30}", end="")
    if (x % 2) == 1:
        print("R${:>7.2f}".format(listagem[x]))
