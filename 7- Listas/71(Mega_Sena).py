'''
Faça um programa que ajude um jogador da MEGA SENA
a criar palpites.O programa vai perguntar quantos jogos
serão gerados e vai sortear 6 números entre 1 e 60
para cada jogo, cadastrando tudo em uma lista composta.
'''

from random import randint
print("~"*20)
print(f"{'JOGA NA MEGA SENA':^20}")
print("~"*20)
lista = list()
princ = list()
count = tot = 0
quantidade = int(input("Digite a quantiade de jogos: "))
while tot < quantidade:
    count = 0
    while True:
        n = randint(0, 60)
        if n not in lista:
            lista.append(n)
            count += 1
        if count == 6:
            break
    lista.sort()
    princ.append(lista[:])
    lista.clear()
    tot += 1
print("~"*8, f"{'Jogos Criados'}", "~"*8)
for i, c in enumerate(princ):
    print(f"Jogo {i+1}: {c}")



