'''
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
'''

aluno = dict()
aprovado = False
resultado = ''

aluno['nome'] = input("Digite o nome do aluno: ")
aluno['media'] = float(input("Digite a media do aluno: "))

if aluno['media'] >= 7:
    aprovado = True
    resultado = 'Aprovado'
else:
    resultado = 'Em recuperação'
    aprovado = False
print("------------------Resultado-----------------")
print(f"Nome: {aluno['nome']}\nMédia: {aluno['media']}\nSituação: {resultado}")
print("------------------Estrutura-----------------")
for k, v in aluno.items():
    print(f"{k} = {v}")