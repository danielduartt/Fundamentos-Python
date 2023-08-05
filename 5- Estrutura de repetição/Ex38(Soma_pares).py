'''
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.
'''
soma = 0
for i in range(0,6):
    num = int(input("digite o numero {}: ".format(i+1)))
    if num % 2 == 0:
        soma += num

print("A soma dos números pares digitados é: {}".format(soma))
