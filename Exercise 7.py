valor = int(input("Digite a quantidade de números que você quer colocar: "))
soma = 0
for i in range(valor):
    num = int(input("Digite um número: "))
    soma += num
media = soma/valor
print(f"A média desses números é {media:.2f}!")