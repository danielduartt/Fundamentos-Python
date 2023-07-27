'''
Faça um programa que leia o nome de 4 alunos(sem o for ou while) e escolha um entre eles aleatoriamente
'''

import random
aluno1 = input("Digite o aluno 1: ")
aluno2 = input("Digite o aluno 2: ")
aluno3 = input("Digite o aluno 3: ")
aluno4 = input("Digite o aluno 4: ")
lista = [aluno1, aluno2, aluno3, aluno4]
aleatorio = random.choice(lista) #escolhe valores da lista
print("O aluno escolhio foi {}".format(aleatorio))
print("-"*40)
print("O aluno escolhio foi {}".format(lista[random.randint(0,3)]))