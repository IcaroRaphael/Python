#Exemplo 1:
teste = list()
teste.append("Gustavo")
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = "Maria"
teste[1] = 22
galera.append(teste[:])
print(galera)

#Exemplo 2:
galera = [["Gustavo", 40], ["Maria", 22]]
print(galera)

#Exemplo 3:
galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:])
    dado.clear()
print(galera)
