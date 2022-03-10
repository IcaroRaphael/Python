"""
Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
"""
r1 = float(input("1º reta: "))
r2 = float(input("2º reta: "))
r3 = float(input("3º reta: "))

if (r2 + r3) > r1 and (r1 + r3) > r2 and (r1 + r2) > r3:
    print("As retas podem formar um triângulo.")
    if r1 == r2 and r2 == r3:
        print("Tipo: Equilátero")
    elif (r1 == r2 and r1 != r3) or (r1 == r3 and r1 != r2) or (r2 == r3 and r2 != r1):
        print("Tipo: Isósceles")
    elif (r1 != r2) and (r1 != r3) and (r2 != r3):
        print("Tipo: Escaleno")
else:
    print("As retas não podem formar um triângulo.")
