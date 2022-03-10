"""
Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final,
mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
individualmente.
"""
primário = list()
secundário = list()
while True:
    # Cadastro
    nome = str(input("Nome: ")).title().strip()
    secundário.append(nome)
    nota1 = float(input("Nota 1: "))
    secundário.append(nota1)
    nota2 = float(input("Nota 2: "))
    secundário.append(nota2)
    média = (nota1 + nota2)/2
    secundário.append((média))
    primário.append(secundário[:])
    secundário.clear()
    # Stop
    stop = ""
    while (stop != "S") and (stop != "N"):
        stop = str(input("Você deseja continuar? [S/N]:")).upper().strip()
    if stop == "N":
        print("-=-"*10)
        break
    print("-=-"*10)
# Boletim
print(f"{'Nº':<4}{'NOME':<12}{'MÉDIA':<10}")
print("-"*30)
for x in range(0, len(primário)):
    print(f"{x:<4}{primário[x][0]:<12}{primário[x][3]:<10}")
print("-"*30)
# Detalhes
stop = 0
while stop != 999:
    stop = int(input("Mostrar as notas de qual aluno? (999 interrompe):"))
    if (stop >= 0) and (stop < len(primário)):
        print(f"Notas de {primário[stop][0]} são [{primário[stop][1]}, {primário[stop][2]}]")
    print("-" * 30)
