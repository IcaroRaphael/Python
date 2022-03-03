"""
Faça um programa que leia nome e média de um aluno, guardando também em um dicionário. No final, mostre o conteúdo
da estrutura na tela.
"""
boletim = dict()
boletim["Nome"] = str(input("Nome: ")).title().strip()
boletim["Média"] = float(input("Média: "))
if boletim["Média"] >= 7:
    boletim["Situação"] = "Aprovado!"
else:
    boletim["Situação"] = "Reprovado!"
print("-=-"*10)
print(f"Nome: {boletim['Nome']}")
print(f"Média: {boletim['Média']}")
print(f"Situação: {boletim['Situação']}")
