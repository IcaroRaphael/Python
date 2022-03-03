frase = "Curso em Video Python"

print("""Geralmente, entendemos o texto como um conjunto de frases, ou seja, algo que foi feito para ser lido.
Mas a definição de texto não é tão simples quanto parece. Imagine, por exemplo, que você está lendo 
um livro e, de repente, encontra em uma página qualquer um papel com a palavra “madeira”.""")

print(frase[::2])
print(frase.count("o"))
print(frase.upper().count("O"))
print(len(frase))
print(len(frase.strip()))
print(frase.replace("Python", "Android"))
print("Curso" in frase)
print(frase.find("Curso"))
print(frase.split())

dividido = frase.split()
print(dividido[0][0])
