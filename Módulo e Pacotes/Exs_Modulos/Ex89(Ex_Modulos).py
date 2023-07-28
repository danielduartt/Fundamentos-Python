'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.
'''

import moeda
#Parte 1
num = float(input("Digite o valor em R$: "))
print(f"*Aumentando 10% fica {moeda.formatacao(moeda.aumentar(num))}") #confuso ein lç6
print(f"*Diminuindo 10% fica {moeda.formatacao(moeda.diminuit(num))}")
print(f"*Dobro: {moeda.formatacao(moeda.dobro(num))}")
print(f"*Metade: {moeda.formatacao(moeda.metade(num))}")
