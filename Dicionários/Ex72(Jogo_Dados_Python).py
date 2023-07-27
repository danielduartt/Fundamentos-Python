'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados
aleatórios. Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor
tirou o maior número no dado.
'''

from random import randint
from time import sleep
from operator import itemgetter
maior = 0

resultados = dict()
resultados['Player 01'] = randint(1, 6)
resultados['Player 02'] = randint(1, 6)
resultados['Player 03'] = randint(1, 6)
resultados['Player 04'] = randint(1, 6)
count = 0
for k, v in resultados.items():
    print(f"{k} tirou {v}")
    if v > maior:
        maior = v
    sleep(1)
#sorted ..... cria tuplas dentro de uma lista
ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True) #1 = ordem de valor
print("~"*20, "Ranking", "~"*20)
count = 1
for k, v in enumerate(ranking):
    print(f"{count}° lugar = {v[0]} com {v[1]}")
    count += 1