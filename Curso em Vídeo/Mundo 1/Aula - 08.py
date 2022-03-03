"""
MÉTODO 1:
import math
num = math.sqrt(raiz)
- Obs: Mais memória, importa todos os itens da biblioteca

# MÉTODO 2:
from math import sqrt
num = sqrt(raiz)
- Obs: Menos memória, importa apenas um item específico


from math import sqrt
num = int(input("Digite um número: "))
raiz = sqrt(num)
print("A raíz de {:.2f} é igual a {:.2f}".format(num, raiz))
"""

import random
num = random.randint(1, 10)
print(num)
