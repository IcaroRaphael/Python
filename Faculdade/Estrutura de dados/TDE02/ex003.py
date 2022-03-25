"""
3.Reverso do número. Faça uma função que retorne o reverso de um número inteiro
informado
"""
num = int(input("Insira um número: "))
string = str(num)
num = int(string[::-1])
print(f"Reverso do número: {num}")
