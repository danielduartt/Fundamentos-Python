'''
Faça um programa que calcule a soma entre todos os números que são múltiplos de três
e que se encontram no intervalo de 1 até 500
'''
soma = 0
count = 0
for c in range(1, 501):
    if c % 3 == 0:
        soma = soma + c
        count += 1
print("A soma de todos os multiplos de 3 no intervalo de 1 até 500 é: {}".format(soma))