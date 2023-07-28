'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.
'''

import moeda

num = float(input("Digite o valor em R$: "))
print(f"Aumentando 10% fica {moeda.aumentar(num)}")
print(f"Diminuindo 10% fica {moeda.diminuit(num)}")
print(f"Dobro: {moeda.dobro(num)}")
print(f"Metade: {moeda.metade(num)}")