"""
Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A";
- Em que posição ela aparece a primeira vez;
- Em que posição ela apece a última vez;
"""
frase = input("Insira uma frase: ")
frase = frase.lower()
print("Quantas vezes aparece a letra 'A'? R:{}".format(frase.count("a")))
print("Em que posição aparece a primeira vez? R:{}".format(frase.find("a")+1))
print("Em que posição aparece a última vez? R:{}".format(frase.rfind("a")+1))
"""
x = len(frase) - 1
while x > 0:
    if "a" == frase[x]:
        print("Em que posição aparece a última vez? R:{}".format(x + 1))
        x = 0
    x = x - 1
"""
