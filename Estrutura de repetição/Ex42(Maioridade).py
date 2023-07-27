#Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores.

from datetime import date
anoAtual = date.today().year
maioridade = 0
menoridade = 0

for i in range(1, 8):
    ano = int(input(f"Digite o ano de nascimento da pessoa {i}: "))
    idade = anoAtual - ano
    if idade >= 18:
        maioridade += 1
    else:
        menoridade += 1

print(f"Pessoas na maioridade: {maioridade}\nPessoas na menoridade: {menoridade}")