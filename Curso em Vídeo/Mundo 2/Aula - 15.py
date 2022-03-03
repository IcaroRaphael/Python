n = s = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s += n
#print("Soma: {}".format(s))
print(f"Soma: {s}")
