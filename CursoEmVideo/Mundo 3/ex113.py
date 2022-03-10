"""
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um
número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""
def leiaInt(frase="Digite um número inteiro: "):
    while True:
        try:
            inteiro = str(input(frase))
            inteiro = int(inteiro)
            break
        except KeyboardInterrupt:
            inteiro = 0
            print("\033[31mUsuário preferiu não digitar esse número.\033[m")
            break
        except ValueError:
            print("\033[31mERRO! Digite um número inteiro válido.\033[m")
    return inteiro


def leiaFloat(frase="Digite um número real: "):
    while True:
       try:
           real = str(input(frase))
           real = float(real)
           break
       except KeyboardInterrupt:
           real = 0
           print("\033[31mUsuário preferiu não digitar esse número.\033[m")
           break
       except ValueError:
           print("\033[31mERRO! Digite um número real válido.\033[m")
    return real


inteiro = leiaInt()
real = leiaFloat()
print(f"Valor inteiro digitado: {inteiro}")
print(f"Valor real digitado: {real}")
