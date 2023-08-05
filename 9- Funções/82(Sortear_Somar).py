'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai
mostrar a soma entre todos os valores pares sorteados pela função anterior.
'''
from random import randint

def sortear(lista):
    for i in range(0, 5):
        lista.append(randint(1, 10))

def somaPar(lst):
    soma = 0
    for i in range(0, len(lst)):
        if lst[i] % 2 == 0:
            soma += lst[i]
    print(f"A soma dos pares é {soma}")

numero = list()
sortear(numero)
print(numero)
somaPar(numero)