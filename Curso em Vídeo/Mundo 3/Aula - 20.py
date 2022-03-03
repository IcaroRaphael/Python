"""
#FUNÇÃO SOMA:
def soma(x, y):
    s = x + y
    print(s)


soma(1, 2)
soma(9, 8)
soma(4, 5)

#FUNÇÃO SOMA COM EMPACOTADOR:
def contador(* num):
    soma = 0
    for n in num:
        soma += n
    print(soma)


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
"""
def dobra(lista):
    p = 0
    while p < len(lista):
        lista[p] *= 2
        p += 1


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)
