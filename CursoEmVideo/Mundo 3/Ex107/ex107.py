"""
Crie um módulo chamado moeda.py que tenha as seguintes funções incorporadas:
- aumentar()
- diminuir()
- dobro()
- metade()

Faça também um programa que importe esse módulo e use algumas dessas funções.
"""
import moeda

preço = float(input("Digite o preço: R$"))
print(f"A metade de {preço} é {moeda.metade(preço)}")
print(f"O dobro de {preço} é {moeda.dobro(preço)}")
print(f"Aumentando 10% de {preço}, temos {moeda.aumentar(preço, 10)}")
print(f"Reduzindo 13% de {preço}, temos {moeda.diminuir(preço, 13)}")
