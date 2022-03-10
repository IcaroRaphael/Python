"""
Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem,
cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.
"""
distancia = float(input("A viagem tem quantos KM: "))
if distancia <= 200:
    passagem = 0.5 * distancia
    print("Preço da passagem: R${:.2f}.".format(passagem))
else:
    passagem = 0.45 * distancia
    print("Preço da passagem: R${:.2f}".format(passagem))
print("Boa Viagem!")