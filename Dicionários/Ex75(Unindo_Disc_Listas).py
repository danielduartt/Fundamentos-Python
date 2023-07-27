'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um
dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''
pessoas = list()
idades = 0
indv = dict()

while True:
    indv['nome'] = input("Nome da pessoa: ")
    indv['idade'] = int(input("Idade: "))
    idades += indv['idade']
    indv['sexo'] = input("Sexo[M,F]: ").strip().upper()[0]
    pessoas.append(indv.copy())
    resp = input("Deseja continuar[S/N]: ").strip().upper()[0]
    if resp == 'N':
        print(">>>Encerrando<<<")
        break

media = idades / len(pessoas)
print("~"*40)
print(f"Quantidade de pessoas cadastradas: {len(pessoas)}")
print(f"Média da idades: {media:.2f}")
print("=-==-=-=- LISTA DE MULHERES =-=-=-=-")
for i in range(0, len(pessoas)):
    if pessoas[i]['sexo'] == 'F':
        print(f"    *{pessoas[i]['nome']}")
print("-=-=-= PESSOAS COM IDADE ACIMA DA MÉDIA =-=-=- ")
for i in range(0, len(pessoas)):
    if pessoas[i]['idade'] > media:
        print(f"    *{pessoas[i]['nome']}")




