"""
Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros
"""
print("CONVERSOR METROS PARA TODAS AS UNIDADES")
m = float(input("Insira o valor em metros: "))
print("Valor Inserido: {} m".format(m))
km = m / 1000
hm = m / 100
dam = m / 10
m = m
dm = m * 10
cm = m * 100
mm = m * 1000
print("Para KM: {}".format(km))
print("Para HM: {}".format(hm))
print("Para DAM: {}".format(dam))
print("PARA M: {}".format(m))
print("Para DM: {}".format(dm))
print("Para CM: {}".format(cm))
print("Para MM: {}".format(mm))
