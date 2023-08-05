'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
notas de cada aluno individualmente.
'''

princ = list()
alunos = list()

while True:
    nome = str(input("Nome do aluno(a): "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    princ.append(alunos[:])
    alunos.clear()
    resp = input("Deseja continuar[S/N]: ").strip().upper()[0]
    if resp == 'N':
        print("Encerrando...")
        break

print(princ)
print("=-="*5, f"{' BOLETIM '}", "=-="*5)
print(f"{'No.':<4}", f"{'Nome':<10}", f"{'Média':>8}")
for i, a in enumerate(princ):
    print(f'{i}{a[0]}{a[2]}')

