"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo
usuário. O programa será interrompido quando o número solicitado for negativo.
"""
while True:
    cont = 1
    tabuada = int(input("Tabuada: "))
    print("-=-"*10)
    if tabuada < 0:
        break
    while cont <= 10:
        print(f"{tabuada} x {cont} = {tabuada*cont}")
        cont += 1
    print("-=-"*10)
print("Fim!")