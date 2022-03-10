"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import date
atual = date.today().year

nascimento = int(input("Ano de Nascimento: "))

if (atual - nascimento) < 18:
    print("Ainda faltam {} ano(s) para se alistar.".format(18-(atual-nascimento)))
elif(atual - nascimento) == 18:
    print("Você deve se alistar esse ano!")
elif(atual - nascimento) > 18:
    print("Já faz {} ano(s) que você deveria se alistar.".format((atual-nascimento)-18))
