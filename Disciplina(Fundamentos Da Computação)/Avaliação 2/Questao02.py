'''
Escreva um programa em python que leia uma lista de números
inteiros até que o usuário digite -1.
A seguir leia dois números,pesquiseos na lista e informe se os numeros foram encontrados ou não. (3pts)
'''

num = []
while True:
    num.append(int(input('Digite um número: ')))
    resp = int(input('Você deseja continuar [1=sim, -1=não]: '))
    if resp == -1:
        print('Ok!, seu desejo é uma ordem')
        print()
        break
print('-='*30)
for x in range(1, 3):
    pesq = int(input(f'Digite o n{x} para saber se ele está na lista: '))
    print()
    if pesq in num:
        print(f'O número {pesq} foi encontrado na lista')
        print('-='*30)
    else:
        print(f'O número {pesq} não foi encontrado na lista')
        print('-='*30)