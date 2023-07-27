'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
'''

while True:
    print("~"*40)
    num = int(input("Digite um número para saber sua tabuada: "))
    print("~" * 40)
    if num < 0:
        print("Programa encerrado! ")

        break
    else:
        for i in range(0,11):
            print(f"{num} x {i} = {num * i}")
