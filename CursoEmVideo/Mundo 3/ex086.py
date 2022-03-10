"""
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final mostre a matriz na tela com a formatação correta.
"""
matriz = [[], [], []]
for x in range(0, 3):
    for y in range(0, 3):
        matriz[x].append(int(input(f"Insira o valor de [{x}][{y}]: ")))
for x in range(0, 3):
    for y in range(0, 3):
        print(f"[{matriz[x][y]:^5}]", end="")
    print()
