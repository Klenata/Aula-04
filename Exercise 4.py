num = int(input("Digite um número inteiro maior que 0: "))
if num == 0:
    print("Numero invalido...")
if num < 0:
    for i in range(num,0):
        print(i, end=" ")
else:
    for i in range(1,num+1):
        print(i, end=" ")