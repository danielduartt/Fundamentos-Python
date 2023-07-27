'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''

from random import randint
maior = menor = 0
tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(tupla)
print(f"Maior: {max(tupla)}\nMenor: {min(tupla)}")
