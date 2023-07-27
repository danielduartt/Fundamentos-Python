'''
Aprimore o desafio 74 para que ele funcione com vários jogadores, incluindo um sistema de visualização
 de detalhes do aproveitamento de cada jogador.
'''
total = 0
jogadores = list()
jogador = dict()
gols = list()

while True:
    total = 0
    jogador['nome'] = input("Digite o nome do jogador: ")
    partidas = int(input(f"Digite quantas partidas {jogador['nome']} jogou: "))
    for i in range(0, partidas):
        gol = int(input(f"  =>Digite a quantidades de gols no jogo {i + 1}: "))
        total += gol
        gols.append(gol)
    jogador['Gols p/ partida'] = gols[:]
    jogador['Total de Gols'] = total
    jogadores.append(jogador.copy())
    gols.clear()
    resp = input("Deseja continuar[S/N]: ").strip().upper()[0]
    if resp == 'N':
        print(">>>Encerrando<<<")
        break

for i in range(0, len(jogadores)):
    print(f"-=-=-=-=-=-=-= Gols por Partida do jogador {jogadores[i]['nome'].strip()}-=-=-=-==-=-=-=-=-=-")
    for c in range(0, len(jogadores[i]['Gols p/ partida'])):
        print(f"    *Partida {c + 1} = {jogadores[i]['Gols p/ partida'][c]}", end='')
        print(" gol" if jogadores[i]['Gols p/ partida'][c] == 1 else " gols" )








