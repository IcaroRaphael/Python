"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número
a calcular e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela
o processo de cálculo do fatorial.
"""
def fatorial(número, show=False):
    '''
    fatorial(n, show=False)
    -> Calcula o fatorial de um número.
    :param número: Valor a ser calculado;
    :param show: (Opcional), mostrar ou não mostrar o cálculo. Escolher usando True ou False.
    :return: Sem retorno.
    '''
    fatorial = 1
    if show == False:
        for x in range(número, 0, -1):
            fatorial *= x
        print(f"{número}! = {fatorial}")
    elif show == True:
        for x in range(número, 0, -1):
            if x > 1:
                print(f"{x} x ", end="")
                fatorial *= x
            elif x == 1:
                print(f"{x} = ", end="")
                fatorial *= x
        print(f"{fatorial}")


número = int(input("Insira o número: "))
resp = ""
while (resp != "S") and (resp != "N"):
    resp = str(input("Você deseja visualizar o cálculo? [S/N]:")).upper().strip()
if resp == "S":
    show = True
elif resp == "N":
    show = False
fatorial(número, show)
