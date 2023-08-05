'''
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
'''

def ficha(nome = '>desconhecido<', gols = 0):

    print(f"O jogador {nome} fez {gols} ", end='')
    print("gols" if gols > 1 else "gol")



name = input("Digite o nome do jogador: ")
pontos = str(input("Digite a quantidade de gols: "))[0]
if pontos.isnumeric():
    pontos = int(pontos)
else:
    pontos = 0

if name.strip() == '':
    ficha(gols=pontos)
else:
    ficha(name, pontos)


