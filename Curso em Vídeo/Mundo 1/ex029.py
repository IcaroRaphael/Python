"""
Escreva um programa que leia a velocidade de um carro.
- Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
- A multa vai custar R$7,00 por cada km/h acima do limite.
"""
velocidade = int(input("Insira a velocidade: "))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print("Você estava acima do limite a {}km/h. A multa vai ser de R${}.".format(velocidade, multa))
else:
    print("Você está dentro do limite de velocidade a {}km/h, pode seguir!".format(velocidade))
