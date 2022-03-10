"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:
- Média abaixo de 5.0: Reprovado
- Média entre 5.0 e 7.0: Recuperação
- Média 7.0 ou superior: Aprovado
"""
print("CALCULADORA DE MÉDIA")
nota1 = float(input("1º Nota: "))
nota2 = float(input("2º Nota: "))
media = (nota1 + nota2)/2
if media < 5:
    print("Média: {}".format(media))
    print("Reprovado!")
elif media >= 5 and media < 7:
    print("Média: {}".format(media))
    print("Recuperação!")
elif media >= 7:
    print("Média: {}".format(media))
    print("Aprovado!")
