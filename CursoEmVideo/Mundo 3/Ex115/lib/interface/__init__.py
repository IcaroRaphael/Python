def leiaint(frase="Digite um número inteiro: "):
    while True:
        try:
            inteiro = int(input(frase))
        except KeyboardInterrupt:
            print("\033[31mUsuário preferiu não digitar esse número.\033[m")
            return 0
        except ValueError:
            print("\033[31mERRO! Digite um número inteiro válido.\033[m")
            continue
        else:
            return inteiro


def linha(tamanho=42):
    l = "-"*tamanho
    return l


def cabeçalho(texto):
    print(linha())
    print(texto.center(42))
    print(linha())


def menu(lista):
    cabeçalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f"\033[33m{c}\033[m - \033[34m{item}\033[m")
        c += 1
    print(linha())
    opção = leiaint("\033[32mSua opção: \033[m")
    return opção

