numero = 0
numero2 = 0
for i in range(10):
    num = int(input("Digite um número: "))
    if 10 <= num <= 20:
        numero +=1
    else:
        numero2 +=1
print(" ")
print(f"Você digitou {numero} números entre 10 e 20 e\n{numero2} números fora deste intervalo!")