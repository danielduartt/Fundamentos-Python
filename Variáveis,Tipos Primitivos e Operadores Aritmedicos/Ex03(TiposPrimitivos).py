'''
    int = inteiro
    float = fracionário
    bool = booleano
    string = str = nome
'''

'''
    Sintaxe print:
    1- print("Oi, nome".format(nome))
    2- print(f"Oi, {nome}") 
'''

#Crie um programa que leia 2 números inteiros e some o valor deles

n1 = int(input("Digite o número 1: "))
n2 = int(input("Digite o número 2: "))
soma = n1 + n2

print( f"A soma de {n1} com {n2} é = {soma}")