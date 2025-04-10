negative = 0
for i in range(10):
    num = int(input("Digite um número: "))
    if num < 0:
        negative +=1
print(f"Você digitou {negative} números negativos!")