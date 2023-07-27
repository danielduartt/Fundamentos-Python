'''
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''

def Maior(*num):
    maior = 0
    if len(num) == 0:
        print("Sem valores digitados!")
        print("Maior valor nao existe")
    else:
        for i in range(0, len(num)):
            if num[i] > maior:
                maior = num[i]
        print(f"O maior valor da sequência é {maior}")


Maior(1, 2, 3, 4, 54, 2, 829, 3201, 100023, 23, 0)
print("-"*20)
Maior()


