"""
Crie um programa que tenha uma tupla com várias palavras(não usar acentos). Depois disso, você deve mostrar,
para cada palavra, quais são as suas vogais.
"""
tupla = ()
while True:
    stop = ""
    str1 = str(input("Insira uma palavra: ")).upper().strip()
    tupla = tupla + (str1,)
    while (stop != "S") and (stop != "N"):
        stop = str(input("Você deseja continuar[S/N}? R:")).upper().strip()
    if stop == "N":
        print("-=-" * 15)
        break
    print("-=-"*15)
for x in range(0, len(tupla)):
    cont = 0
    print(f"Na palavra {tupla[x]} temos as vogais: ", end="")
    for y in range(0, len(tupla[x])):
        if tupla[x][y] in "AEIOU":
            print(f"{tupla[x][y]} ".lower(), end="")
            cont += 1
    if cont == 0:
        print("Nenhuma vogal encontrada!", end="")
    print()
