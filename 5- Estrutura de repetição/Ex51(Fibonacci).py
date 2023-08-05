'''
Escreva um programa que leia um número N inteiro qualquer e
mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
'''
print("~"*25)
print("Sequência de Fibonacci")
print("~"*25)
n = int(input("Entre com o N: "))
primeiro = 0
segundo = 1
terceiro = primeiro + segundo
count = 3
print(f"{primeiro} - {segundo}", end = '')
while count != n:
    primeiro = segundo
    segundo = terceiro
    terceiro = primeiro + segundo
    print(f" - {terceiro}", end='')
    if count == n - 1:
        print('.')
    count += 1


