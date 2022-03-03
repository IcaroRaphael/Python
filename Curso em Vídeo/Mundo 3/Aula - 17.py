"""
#Adicionar elementos ao final da lista
lista.append("Elemento")

#Inserir elementos em qualquer posição da lista
lista.insert(posição, "elemento")

#Apagar elementos de uma lista
del lista[posição]
lista.pop(posição)
lista.remove("elemento")

#Apagar o último elemento da lista
lista.pop()

#Estrutura de lista usando range
valores = list(range(4, 11))
valores: [4, 5, 6, 7, 8, 9, 10]

#Colocando uma lista em ordem crescente
lista.sort()

#Colocando uma lista em ordem decrescente
lista.sort(reverse=True)

#Sabendo o tamanho de uma lista
len(lista)

#Criando lista vazia
lista = lista()
lista = []

#Pegando a chave e os valores de cada chave
for c, v in enumerate(valores):
    print(f"Na posição {c} encontrei o valor {v}")

#Inserindo valores a listas
for c in range(0, 5):
    valores.append(int(input("Digite um valor: ")))

#Criando cópia de uma lista
a = [1, 2, 3, 4, 5]
b = a[:]
"""
