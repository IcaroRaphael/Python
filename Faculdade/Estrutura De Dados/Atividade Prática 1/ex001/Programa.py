"""
1 - Construa uma Pilha utilizando a linguagem Python. Dada uma sequência contendo N (N > 0) números inteiros,
imprimi-la na ordem inversa.
"""

import numpy as np


class Pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.topo = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def pilhaCheia(self):
        if self.topo == self.capacidade - 1:
            return True
        else:
            return False

    def pilhaVazia(self):
        if self.topo == -1:
            return True
        else:
            return False

    def empilhar(self, valor):
        if self.pilhaCheia():
            print('A Pilha está cheia')
        else:
            self.topo += 1
            self.valores[self.topo] = valor

    def desempilhar(self):
        if self.pilhaVazia():
            print('A pilha está vazia')
            return -1
        else:
            valor = self.valores[self.topo]
            self.topo -= 1
            return valor

    def verTopo(self):
        if self.topo != -1:
            return self.valores[self.topo]
        else:
            return -1

    def mostrarInversa(self):
        if pilha.pilhaVazia():
            print("A pilha está vazia!")
        else:
            print("Ordem inversa: ", end="")
            for valor in range(self.capacidade-1, -1, -1):
                print(f"{pilha.valores[valor]} ", end="")


quant = int(input('Quantos números serão lidos? R:'))
pilha = Pilha(quant)

# Inserindo valores a pilha
for valor in range(quant):
    if pilha.pilhaCheia():
        print("A pilha está cheia!")
    else:
        numero = int(input(f"{valor+1}º número: "))
        pilha.empilhar(numero)

print("-=-"*15)
pilha.mostrarInversa()
