"""
- aumentar()
- diminuir()
- dobro()
- metade()
"""
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
    metade = valor / 2
    return metade
