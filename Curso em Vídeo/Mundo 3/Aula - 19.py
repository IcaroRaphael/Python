"""
pessoas  = {"Nome": "Gustavo", "Sexo": "Masculino", "Idade": 22}
print(f"O {pessoas['Nome']} tem {pessoas['Idade']} anos.")
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for v in pessoas.values():
    print(v)
for i in pessoas.items():
    print(i)
del pessoas["Sexo"]
pessoas["Nome"] = "Leandro"
pessoas["Peso"] = 98.5
print(pessoas)
brasil = list()
estado1 = {"UF":"Rio de Janeiro", "Sigla":"RJ"}
estado2 = {"UF":"São Paulo", "Sigla":"SP"}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
"""
estado = dict()
brasil = list()
for x in range(0, 3):
    estado["uf"] = str(input("Unidade Federativa: "))
    estado["Sigla"] = str(input("Sigla: "))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f"{k}: {v}")
    print("-=-"*5)