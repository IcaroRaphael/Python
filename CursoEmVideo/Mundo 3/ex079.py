"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""
valores = list()
while True:
    escolha = ""
    valor = int(input("Insira um valor: "))
    if valor in valores:
        print(f"O valor {valor} já está na lista.")
    else:
        valores.append(valor)
    while (escolha != "S") and (escolha != "N"):
        escolha = str(input("Você deseja inserir outro valor [S/N]? R:")).strip().upper()
    if escolha == "N":
        print("-=-" * 20)
        break
    print("-=-"*20)
print(f"Os valores digitados foram: {sorted(valores)}")
