'''
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
'''

def notas(*notas, sit = False):
    turma = dict()
    soma = 0
    for i in notas:
        soma += i
    turma['total'] = len(notas)
    turma['maior'] = max(notas)
    turma['menor'] = min(notas)
    turma['media'] = soma/len(notas)
    if sit:
        if turma['media'] >= 7:
            turma['situação'] = 'aprovado(a)'
        else:
            turma['situação'] = 'recuperação'
    return turma

n= notas(5,4,8,9, sit = True)
print(n)




