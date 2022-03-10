"""
Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando
se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
"""
import moeda

preço = float(input("Digite o preço: R$"))
print(f"A metade de {preço} é {moeda.metade(preço, situação=True)}")
print(f"O dobro de {preço} é {moeda.dobro(preço, situação=True)}")
print(f"Aumentando 10% de {preço}, temos {moeda.aumentar(preço, 10, situação=True)}")
print(f"Reduzindo 13% de {preço}, temos {moeda.diminuir(preço, 13, situação=True)}")
