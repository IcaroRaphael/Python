"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".
"""
cidade = input("Cidade: ")
cidade = cidade.title().split()
if cidade[0] == "Santo":
    print("Sua cidade começa com o nome 'Santo'")
else:
    print("Sua cidade não começa com o nome 'Santo'")
