"""
***** TUPLAS *****
OBS1: AS TUPLAS SÃO IMUTÁVEIS
"""
lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim")
lanche2 = ("Refrigerante", "Batata Frita")
print(lanche)
#União de 2 tuplas
união = lanche + lanche2
print(união)
#Mostrar quantas vezes aparece um elemento
print(lanche.count("Hambúrguer"))
#Mostrar em que posição aparece um elemento
print(lanche.index("Hambúrguer"))
#Apagando uma tupla
del(união)
