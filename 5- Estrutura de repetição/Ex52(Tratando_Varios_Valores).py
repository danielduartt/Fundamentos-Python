'''
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números
foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''
soma = num = 0
while num != 999:
    num = int(input("Digite um número [999 para sair]: "))
    if num < 999:
        soma += num



print("A soma é {}".format(soma))