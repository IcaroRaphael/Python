"""
Crie um pacote chamado utilidades CeV que tenha dois módulos internos chamados moeda e dado.
Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e
mantenha tudo funcionando.
"""
from UtilidadesCeV import Moeda

preço = float(input("Digite o preço: R$"))
Moeda.resumo(preço, 20, 12)
