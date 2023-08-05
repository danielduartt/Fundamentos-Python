#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
num = int(input("Digite um número: "))
count = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end = ' ')
        count += 1
    else:
        print('\033[31m', end=' ')
    print(f"{c}", end = ' ')
print('\033[m')
if count == 2:
    print(f"O número {num} é primo!")
else:
    print(f"O número {num} não é primo")