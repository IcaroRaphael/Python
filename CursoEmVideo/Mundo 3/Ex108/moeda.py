"""
- aumentar()
- diminuir()
- dobro()
- metade()
- moeda(
"""
def moeda(valor=0, moeda="R$"):
    formatado = (f"{moeda}{valor:.2f}".replace(".", ","))
    return formatado


def aumentar(valor=0, percentual=0):
    percentual = (100 + percentual)/100
    valor *= percentual
    return valor


def diminuir(valor=0, percentual=0):
    valor = valor - (valor * percentual / 100)
    return valor


def dobro(valor=0):
    dobro = valor * 2
    return dobro


def metade(valor=0):
    valor = round(valor, 2)
    metade = valor / 2
    return metade
