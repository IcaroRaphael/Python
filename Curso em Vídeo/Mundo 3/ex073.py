"""
Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol,
na ordem de colocação. Depois mostre:
a) Apenas os 5 primeiros colocados.
b) Os últimos 4 colocados da tabela.
c) Uma lista com os times em ordem alfabética.
d) Em que posição da tabela está o time do chapecoense.
"""
brasileirão = ("Atlético Mineiro", "Flamengo", "Palmeiras", "Fortaleza", "Corinthians", "Red Bull Bragantino",
               "Fluminense", "América FC", "Atlético Goianiense", "Santos FC", "Ceará SC", "Internacional",
               "São Paulo FC", "Atlético Paranaense", "Cuiaba Esporte Clube", "EC Juventude", "Gremio FB",
               "EC Bahia", "Sport Clube do Recife", "Chapecoense SC")
#a) Apenas os 5 primeiros colocados.
print("Os 5 primeiros colocados são: ")
for x in range(0, 5):
    print(f"{x+1}º:",brasileirão[x])
print("")
#b) Os últimos 4 colocados da tabela.
print("Os últimos 4 colocados da tabela são: ")
y = 21
for x in range(1, 5):
    x *= -1
    y -= 1
    print(f"{y}º:",brasileirão[x])
print("")
#c) Uma lista com os times em ordem alfabética.
print("Lista dos times do brasileirão em ordem alfabética: ")
ordem = sorted(brasileirão)
for x in ordem:
    print(x)
print("")
#d) Em que posição da tabela está o time do chapecoense.
print(f"O Chapecoense está em {brasileirão.index('Chapecoense SC')+1}º lugar.")
