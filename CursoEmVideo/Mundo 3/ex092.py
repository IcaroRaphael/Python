"""
Crie um programa que leia o nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionário
se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule
e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
#dicionário: nome, idade, carteira de trabalho
import datetime
atual = datetime.now().year
cadastro = dict()
cadastro["Nome"] = str(input("Nome: ")).title().strip()
nascimento = int(input("Ano de Nascimento: "))
cadastro["Idade"] = atual - nascimento
cadastro["Sexo"] = str(input("Sexo[M/F]: ")).upper().strip()
cadastro["CTPS"] = int(input("CTPS: "))
if cadastro["CTPS"] != 0:
    cadastro["Ano de contratação"] = int(input("Ano de contratação: "))
    cadastro["Salário"] = float(input("Salário: "))
    if cadastro["Sexo"] == "M":
        serviço = 35 - (atual - cadastro["Ano de contratação"])
        if serviço < 35:
            cadastro["Aposentadoria"] = cadastro["Idade"] + serviço
        else:
            cadastro["Aposentadoria"] = "Aposentado!"
    elif cadastro["Sexo"] == "F":
        serviço = 30 - (atual - cadastro["Ano de contratação"])
        if serviço < 30:
            cadastro["Aposentadoria"] = cadastro["Idade"] + serviço
        else:
            cadastro["Aposentadoria"] = "Aposentado!"
print("-=-"*20)
for k, v in cadastro.items():
    print(f"{k}: {v}")
