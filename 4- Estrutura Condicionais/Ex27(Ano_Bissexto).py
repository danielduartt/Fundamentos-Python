#crie um programa que lei a um ano e diga se é bissexto ou nao

from datetime import date
#anoAtual = 2023
anoEsc = int(input("Digite o ano que deseja analisar [0 para analisar o ano atual]: "))
if anoEsc == 0:
    anoEsc = date.today().year
if anoEsc % 4 == 0 and anoEsc % 100 != 0 or anoEsc % 400 == 0:
    print("O ano de {} é bissexto!".format(anoEsc))
else:
    print("O ano de {} não é bissexto!".format(anoEsc))