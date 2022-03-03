'''
# Documentação de uma função:
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: Início da contagem;
    :param f: Fim da contagem;
    :param p: Passo da contagem;
    :return: Sem retorno;
    """
    c = i
    while c <= f:
        print(f"{c} ", end="")
        c += p
    print("FIM!")


help(contador)

# Variável A em 2 escopos(Local/Global):
def teste(b):
    a = 8
    b += 4
    c = 2
    print(f"A dentro vale {a}") # a = 5
    print(f"B dentro vale {b}") # b = 9
    print(f"C dentro vale {c}") # c = 2


a = 5
teste(a)
print(f"A fora vale {a}") # a = 5

# Variável A do escopo Global recebendo valor do escopo Local:
def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f"A dentro vale {a}")  # a = 8
    print(f"B dentro vale {b}")  # b = 9
    print(f"C dentro vale {c}")  # c = 2


a = 5
teste(a)
print(f"A fora vale {a}")  # a = 8

# Retorno de valores:
def somar(a = 0, b = 0, c = 0):
    s = a + b + c
    return(s)


resp = somar(3, 2, 5)
print(resp)
resp = somar(2, 2)
print(resp)
resp = somar(6)
print(resp)

# Método 1:
def fatorial(n):
    fatorial = 1
    max = n+1
    for x in range(1, max):
        if x == 1:
            print(f"{x} x ", end="")
            fatorial *= x
        elif (x > 1) and (x < (max-1)):
            print(f"{x} x ", end="")
            fatorial *= x
        elif x == (max-1):
            print(f"{x} = ", end = "")
            fatorial *= x
    print(fatorial)

número = int(input("Insira um número: "))
fatorial(número)

'''
# Método 2:
def fatorial(n=1):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f


n = int(input("Insira o número: "))
print(f"{n}! = {fatorial(n)}")
