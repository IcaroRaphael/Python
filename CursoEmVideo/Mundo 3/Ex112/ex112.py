"""
Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada
leiaDinheiro() que seja capas de funcionar como a função input(), mas com uma validação de dados para aceitar
apenas valores que sejam monetários.
"""
from UtilidadesCeV import Moeda
from UtilidadesCeV import Dados

p = Dados.leiadinheiro()
Moeda.resumo(p, 80, 35)
