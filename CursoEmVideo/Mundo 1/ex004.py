a = input("Digite algo: ")
print("O tipo desse valor é: {}".format(type(a)))
print("Só tem espaços? R:{}".format(a.isspace()))
print("É um número? R:{}".format(a.isnumeric()))
print("É alfabético? R:{}".format(a.isalpha()))
print("É alfanumérico? R:{}".format(a.isalnum()))
print("Está em maiúsculas? R:{}".format(a.isupper()))
print("Está em minúsculas? R:{}".format(a.islower()))
print("Está capitalizada? R:{}".format(a.istitle()))
