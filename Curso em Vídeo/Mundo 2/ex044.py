"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
preço normal e condição de pagamento:
- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: Preço normal
- 3x ou mais no cartão: 20% de juros
"""
print("CALCULADORA DE PAGAMENTO\n")
valor = float(input("Valor a ser pago: R$"))
print("-"*40)
print("Métodos de pagamento...")
print("1 - À vista (Dinheiro/Cheque);")
print("2 - À vista (Cartão);")
print("3 - Parcelado em 2x(Cartão);")
print("4 - Parcelado em 3x ou mais (Cartão);")
pagamento = int(input("Forma de pagamento: "))
print("-"*40)

if pagamento == 1:
    print("Valor final: R${:.2f}".format(valor * 0.9))
elif pagamento == 2:
    print("Valor final: R${:.2f}".format(valor * 0.95))
elif pagamento == 3:
    print("2x de R${:.2f}".format(valor/2))
    print("Valor final: R${:.2f}".format(valor))
elif pagamento == 4:
    parcelas = int(input("Quantidade de parcelas: "))
    print("{}x de R${:.2f}".format(parcelas, ((valor*1.2)/parcelas)))
    print("Valor final: R${:.2f}".format(valor * 1.2))
else:
    print("Opção Inválida.")
