"""
4 - Construa uma Fila de Prioridade utilizando a linguagem Python em que sejam
implementadas as funções para inserção de um novo elemento (inteiro) na fila e a
remoção do elemento de mais alta prioridade
"""
import numpy as np


class FilaPrioridade:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.numeroElementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def filaVazia(self):
        return self.numeroElementos == 0

    def filaCheia(self):
        return self.numeroElementos == self.capacidade

    def enfileirar(self, valor):
        if self.filaCheia():
            print("Fila cheia!")
            return
        if self.numeroElementos == 0:
            self.valores[self.numeroElementos] = valor
            self.numeroElementos += 1
        else:
            x = self.numeroElementos - 1
            while x >= 0:
                if valor < self.valores[x]:
                    self.valores[x+1] = self.valores[x]
                else:
                    break
                x -= 1
            self.valores[x+1] = valor
            self.numeroElementos += 1

    def desenfileirar(self):
        if self.filaVazia():
            print("A fila está vazia.")
            return
        valor = self.valores[self.numeroElementos - 1]
        self.numeroElementos -= 1
        return valor

    def verPrimeiro(self):
        if self.filaVazia():
            return - 1
        return self.valores[self.numeroElementos - 1]


# DEFININDO TAMANHO DA FILA
quant = int(input("Quantas elementos serão lidos? R:"))
fila = FilaPrioridade(quant)

# DEFININDO VALORES VAZIOS
for y in range(len(fila.valores)):
    fila.valores[y] = 0

# INSERINDO VALORES NA FILA
while True:
    print("-=-" * 15)
    print("OPERAÇÕES DISPONÍVEIS:")
    print("1 - Inserir elemento;")
    print("2 - Remover elemento de maior prioridade;")
    print("3 - Visualizar elementos;")
    print("4 - Sair do programa;")
    opcao = int(input("Insira uma opção: "))

    print()
    if opcao == 1:
        if fila.filaCheia():
            print("A fila está cheia!")
        else:
            elemento = int(input("Insira um elemento (Diferente de zero): "))
            fila.enfileirar(elemento)

    elif opcao == 2:
        if fila.filaVazia():
            print("A fila está vazia!")
        else:
            print(f"Removendo elemento: {fila.valores[0]}")

    elif opcao == 3:
        if fila.filaVazia():
            print("A fila está vazia!")
        else:
            print(f"Elementos na fila: ", end="")
            for x in range(len(fila.valores)):
                if fila.valores[x] != 0:
                    print(f" {fila.valores[x]}", end="")
            print()

    elif opcao == 4:
        print("Finalizando programa...")
        break

    else:
        print("Opção inválida!")