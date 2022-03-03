"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""
começo = int(input("Primeiro termo: "))
razão = int(input("Razão: "))
for x in range(0, 10):
    print(começo)
    começo = começo + razão
