"""
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do python,
só que fazendo a validação para aceitar apenas um valor numérico.

Ex.:
n = leiaInt("Digite um número: ")
"""
def leiaInt(frase=""):
    numero = str(input(frase))
    if (numero % 2 == 0) or (numero % 2 != 0):
        return numero
    else:
        aviso = "NaN"
        return aviso


n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número: {n}")
