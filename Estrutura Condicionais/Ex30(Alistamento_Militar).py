'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda
vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

from datetime import date
ano = int(input("Digite o ano de nascimento: "))
anoPrevisto = ano + 18
anoAtual = date.today().year
idade = anoAtual - ano
print(f"Quem nasceu em {ano} tem {idade} anos de idade em {anoAtual}")
if idade == 18:
    print("Você precisa se alistar! ")
elif idade > 18:
    print("Você passou {} anos do seu alistamento".format(anoAtual - anoPrevisto))
    print("Você precisa de alistar!")
else:
    print("Ainda faltam {} para se alistar! ".format(anoPrevisto - anoAtual) )
    print("Seu alistamento será em {}".format(anoPrevisto))
