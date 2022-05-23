"""
3 - Construa um programa em Python de acordo com situação problema descrita: Um grupo
de soldados está cercado e não há esperança de vitória, porém existe somente um cavalo
disponível para escapar e buscar por reforços. Para determinar qual soldado deve escapar
para encontrar ajuda, eles formam um círculo (Fila Circular) e sorteiam um número de um
chapéu. Começando por um soldado sorteado aleatoriamente, uma contagem é realizada
até o número sorteado. Quando a contagem terminar, o soldado em que a contagem
parou é removido do círculo, um novo número é sorteado e a contagem recomeça no
soldado seguinte ao que foi eliminado. A cada rodada, portanto, o círculo diminui em um,
até que somente um soldado reste e seja escolhido para a tarefa.
"""
import numpy as np
from random import randint


class FilaCircular:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.fim = -1
        self.numeroElementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def filaVazia(self):
        if self.numeroElementos == 0:
            return True
        else:
            return False

    def filaCheia(self):
        if self.numeroElementos == self.capacidade - 1:
            return True
        else:
            return False

    def enfileirar(self, valor):
        if self.filaCheia():
            print('A fila está cheia')
        else:
            if self.fim == self.capacidade - 1:
                self.fim = -1
            self.fim += 1
            self.valores[self.fim] = valor
            self.numeroElementos += 1

        def desenfileirar(self):
            if self.filaVazia():
                print('A fila está vazia')
            else:
                temp = self.valores[self.inicio]
                self.inicio += 1
                if self.inicio == self.capacidade - 1:
                    self.inicio = 0
                    self.numeroElemento -= 1
                    return temp

        def primeiro(self):
            if self.filaVazia():
                return -1
            else:
                return self.valores[self.inicio]


# FUNÇÃO LINHA
def linha():
    print("\033[1;34m-=-\033[m"*20)


# FUNÇÃO MENSAGEM DE INVALIDEZ
def comandoInvalido():
    print("\033[1;31mOpção inválida. Tente novamente!\033[m")


print("* FILA CIRCULAR *")
# INSERINDO SOLDADOS NA FILA CIRCULAR
while True:
    try:
        linha()
        quant = int(input("Quantidade total de soldados: "))
        break
    except:
        comandoInvalido()
fila = FilaCircular(quant)
if quant > 0:
    for s in range(quant):
        while True:
            try:
                soldado = int(input(f"Nº de identificação do {s+1}º soldado: "))
                break
            except:
                comandoInvalido()
        fila.enfileirar(soldado)
    linha()

    # SORTEANDO SOLDADO
    soldadoEscolhido = 0
    for x in range(len(fila.valores)-1):
        while True:
            aleatorio = randint(0, len(fila.valores)-1)
            if fila.valores[aleatorio] != 0:
                fila.valores[aleatorio] = 0
                break
    for s in range(len(fila.valores)):
        if fila.valores[s] != 0:
            soldadoEscolhido = fila.valores[s]

    # MOSTRANDO SOLDADO ESCOLHIDO
    print(f"Nº Identificação do soldado escolhido: {soldadoEscolhido}")
else:
    print("A fila está vazia!")
