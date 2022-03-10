"""
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do python,
só que fazendo a validação para aceitar apenas um valor numérico.

Ex.:
n = leiaInt("Digite um número: ")
"""
def leiaInt(frase="Digite um número: "):
    while True:
        numero = str(input(frase))
        if numero.isnumeric():
            numero = int(numero)
            break
        else:
            print("\033[31mERRO! Digite um número inteiro válido.\033[m")
    return numero


n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número: {n}")
