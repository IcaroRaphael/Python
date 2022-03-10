"""
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
correta de inserção (SEM USAR O SORT()).
No final, mostre a lista ordenada na tela.
"""
valores = list()
for x in range(0, 5):
    num = int(input("Insira o valor: "))
    if (x == 0) or (num > valores[-1]):
        valores.append(num)
    else:
        p = 0
        while p < len(valores):
            if num <= valores[p]:
                valores.insert(p, num)
                break
            p += 1
print("-=-"*20)
print(f"O resultado foi: {valores}")
                