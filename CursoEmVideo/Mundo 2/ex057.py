"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F".
Caso esteja errado, peça a digitação novamente até um valor correto.
"""
sexo = str(input("Qual seu sexo [M/F]? ")).upper()
while (sexo != "M") and (sexo != "F"):
    sexo = str(input("Dados inválidos! Tente novamente [M/F]: ")).upper().strip()
print("Dados registrados com sucesso!")
