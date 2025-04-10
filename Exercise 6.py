numero = 0
quantidade = 10
for i in range(quantidade):
    num = int(input("Digite um número: "))
    if 10 <= num <= 20:
        numero +=1
numero2 = quantidade - numero
print(" ")
print(f"Você digitou {numero} números entre 10 e 20 e\n{numero2} números fora deste intervalo!")