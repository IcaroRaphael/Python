"""
2 - Desenvolva um programa em Python utilizando uma Pilha de acordo com a situação
problema: Armazene as placas dos carros de luxos (apenas os números) que estão
estacionados em um rua sem saída. Dado uma placa verifique se o carro está estacionado
na rua. Caso esteja, informe a sequência de carros que deverá ser retirada para que o
carro em questão consiga sair.
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

    def verificadorPlaca(self, placa):
        if pilha.pilhaVazia():
            return False
        else:
            i = self.capacidade - 1
            while i >= 0:
                if self.valores[i] == placa:
                    return True
                i -= 1
            return False


quant = int(input('Quantos carros serão lidos? R:'))
pilha = Pilha(quant)

# Inserindo valores a pilha
for valor in range(quant):
    if pilha.pilhaCheia():
        print("A pilha está cheia!")
    else:
        placa = int(input(f"{valor+1}º placa: "))
        pilha.empilhar(placa)

print("-=-"*15)
placa = int(input("Insira a placa do carro escolhido: "))
print("-=-"*15)

cont = pilha.capacidade - 1
if pilha.verificadorPlaca(placa):
    while cont >= 0:
        if placa == pilha.valores[cont]:
            print(f"Carro escolhido saindo! (Placa: {pilha.valores[cont]})")
            break
        else:
            print(f"Removendo carro obstáculo! (Placa: {pilha.valores[cont]})")
            pilha.desempilhar()
        cont -= 1
else:
    print("Placa inserida não existe!")
