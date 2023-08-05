'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols
feitos durante o campeonato.
'''
dados = dict()
dados['nome'] = input("Digite o nome do jogador: ")
partidas = int(input(f"Digite quantas partidas {dados['nome']} jogou: "))
gols = list()
total = 0
for c in range(0, partidas):
        gol = (int(input(f"     Digite a quantidade de gols na partida {c}: ")))
        total += gol
        gols.append(gol)
dados['gols'] = gols[:]
dados['total'] = total
print("=-="*30)
for k, v in dados.items():
    print(f"O campo {k} tem valor {v}")
print("=-="*30)
print(f"O jogador {dados['nome']} jogou {partidas} partidas")
for i in range(0, partidas):
    print(f"=> na partida {i} fez {dados['gols'][i]} gols")

