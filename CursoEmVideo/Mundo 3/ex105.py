"""
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings da função.
"""
def notas(* notas, sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param notas: Uma ou mais notas dos alunos (Aceita várias).
    :param sit: Valor opcional, indicando se deve ou não adicionar situação com (True/False).
    :return: Retorna o dicionário com informações.
    '''
    dicionário = dict()
    cont = soma = 0
    for n in notas:
        soma += n
        if cont == 0:
            maior = n
            menor = n
        else:
            if n > maior:
                maior = n
            elif n < menor:
                menor = n
        cont += 1
    dicionário["Total"] = cont
    dicionário["Maior"] = maior
    dicionário["Menor"] = menor
    média = soma/cont
    dicionário["Média"] = média
    if sit == True:
        if (média >= 7) and (média < 10):
            dicionário["Situação"] = "Boa"
        elif (média < 7):
            dicionário["Situação"] = "Ruim"
        elif (média == 10):
            dicionário["Situação"] = "Excelente"
    return dicionário


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
