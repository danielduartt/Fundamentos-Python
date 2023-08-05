'''
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''
def voto(nascimento):
    from datetime import date #só executa la função = > economiza memória
    anoAtual = date.today().year
    idade = anoAtual - nascimento
    if idade >= 18:
        return f"Idade {idade} Voto: OBRIGATÓRIO"
    elif idade <= 16 or idade >= 65:
        return f"Idade {idade} Voto: OPCIONAL"
    else:
        return f"Idade {idade}: NÃO OBRIGATÓRIO"

nasc = int(input("Digite o ano de nascimento do canditado: "))
print(voto(nasc))

