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


def aumentar(valor=0, percentual=0, situação=False):
    percentual = (100 + percentual) / 100
    valor *= percentual
    if situação:
        formatado = moeda(valor)
        return formatado
    else:
        return valor


def diminuir(valor=0, percentual=0, situação=False):
    valor = valor - (valor * percentual / 100)
    if situação:
        formatado = moeda(valor)
        return formatado
    else:
        return valor


def dobro(valor=0, situação=False):
    dobro = valor * 2
    if situação:
        formatado = moeda(dobro)
        return formatado
    else:
        return dobro


def metade(valor=0, situação=False):
    valor = round(valor, 2)
    metade = valor / 2
    if situação:
        formatado = moeda(metade)
        return formatado
    else:
        return metade
