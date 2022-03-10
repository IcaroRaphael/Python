"""
Aprimore o desafio anterior, mostrando no final;
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da seguna linha.
"""
somapares = somaterceira = 0
matriz = [[], [], []]
for x in range(0, 3):
    for y in range(0, 3):
        matriz[x].append(int(input(f"Insira o valor de [{x}][{y}]: ")))
for x in range(0, 3):
    for y in range(0, 3):
        print(f"[{matriz[x][y]:^5}]", end="")
    print()
# A) A soma de todos os valores pares digitados.
for x in range(0, 3):
    for y in range(0, 3):
        if (matriz[x][y] % 2) == 0:
            somapares += matriz[x][y]
print(f"A) A soma de todos os valores pares digitados: {somapares}")
# B) A soma dos valores da terceira coluna.
for v in range(0, 3):
    somaterceira += matriz[v][2]
print(f"B) A soma dos valores da terceira coluna: {somaterceira}")
# C) O maior valor da seguna linha.
for n in range(0, 3):
    if n == 0:
        maior = matriz[1][n]
    elif matriz[1][n] > maior:
        maior = matriz[1][n]
print(f"C) O maior valor da seguna linha: {maior}")
