def arquivoExiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, "wt+")
        a.close()
    except:
        print("Houve um erro na criação do arquivo!")
    else:
        print(f"Arquivo '{nome}' criado com sucesso!")


def cabeçalho(texto):
    print("-"*42)
    print(texto.center(42))
    print("-"*42)


def lerArquivo(nome):
    try:
        a = open(nome, "rt")
    except:
        print("Erro ao ler o arquivo.")
    else:
        cabeçalho("PESSOAS CADASTRADAS")
        for linha in a:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n", "")
            print(f"{dado[0]:<30}{dado[1]:>3} anos")
    finally:
        a.close()


def cadastrar(arquivo, nome="Desconhecido", idade=0):
    try:
        a = open(arquivo,"at")
    except:
        print("Hoube um erro na abertura do arquivo!")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print("Houve um ERRO na hora de escrever os dados!")
        else:
            print(f"Novo registro de {nome} adicionado.")
