
'''
Escreva um programa em python que leia números inteiros até que o
usuário digite -1. Calcule a porcentagem de números ímpares entre todos
os números digitados. (3pts)
'''

impar = []
par = []
while True:
    num = int(input('Digite os números de sua lista: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    resp = int(input('Deseja continuar? [1=sim, -1=não]: '))
    if resp == -1:
        break
lista = par[:]
lista.extend(impar)
lista.sort()
tamanho1 = len(par)
tamanho2 = len(impar)
print('-='*30)
porcentagem = (tamanho2 * 100) / len(lista)
porcentagem2 = (tamanho1 * 100) / len(lista)
print(f'A lista em ordem Crescente é {lista}')
print(f'Os números pares dela são: {par}')
print(f'Os números impares dela são: {impar}')
print('-='*30)
print('A porcentagem de valores impares é {:.2f}%'.format(porcentagem))
print('Portanto a porcentagem de valores pares é {:.2f}%'.format(porcentagem2))
