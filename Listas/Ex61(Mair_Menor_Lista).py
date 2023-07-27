'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''

valores = list()
for c in range(1, 6):
    valores.append(int(input(f"Digite um número na posição {c}: ")))
print(f"Lista:{valores}")
valores.sort()
ultimo = len(valores)
print(f"Maior: {valores[ultimo-1]}\tPosição: {ultimo-1}")
print(f"Menor: {valores[0]}\tPosição: 0")