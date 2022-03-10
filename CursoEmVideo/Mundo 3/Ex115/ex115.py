"""
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto
simples.
O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
"""
from lib.interface import *
from lib.arquivo import *
from time import sleep

arquivo = "CursoEmVideo.txt"

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do sistema"])
    if resposta == 1:
        #Opção de listar o conteúdo de um arquivo
        lerArquivo(arquivo)
    elif resposta == 2:
        #Opção de cadastrar uma nova pessoa
        cabeçalho("NOVO CADASTRO")
        nome = str(input("Nome: ")).title().strip()
        idade = leiaint("Idade: ")
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        cabeçalho("Saindo do sistema... Até logo!")
        break
    else:
        print("\033[31mERRO! Digite uma opção válida!\033[m")
    sleep(1)
