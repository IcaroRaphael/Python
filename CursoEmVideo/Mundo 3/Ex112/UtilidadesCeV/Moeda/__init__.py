"""
- aumentar()
- diminuir()
- dobro()
- metade()
- moeda()
"""
def moeda(valor=0, moeda="R$"):
    formatado = (f"{moeda}{valor:.2f}".replace(".", ","))
    return formatado


def aumentar(valor=0, percentual=0):
    percentual = (100 + percentual) / 100
    valor *= percentual
    formatado = moeda(valor)
    return formatado


def diminuir(valor=0, percentual=0):
    valor = valor - (valor * percentual / 100)
    formatado = moeda(valor)
    return formatado


def dobro(valor=0):
    dobro = valor * 2
    formatado = moeda(dobro)
    return formatado


def metade(valor=0):
    valor = round(valor, 2)
    metade = valor / 2
    formatado = moeda(metade)
    return formatado


def resumo(valor=0, aumento=0, redução=0):
    print("-"*30)
    print(f"{'RESUMO DO VALOR':^30}")
    print("-" * 30)
    print(f"{'Preço analisado:':<20}", end="")
    print(moeda(valor))
    print(f"{'Dobro do preço:':<20}", end="")
    print(dobro(valor))
    print(f"{'Metade do Preço:':<20}", end="")
    print(metade(valor))
    print(f"{aumento}% {'de aumento:':<16}", end="")
    print(aumentar(valor, aumento))
    print(f"{redução}% {'de redução:':<16}", end="")
    print(diminuir(valor, redução))
    print("-" * 30)
