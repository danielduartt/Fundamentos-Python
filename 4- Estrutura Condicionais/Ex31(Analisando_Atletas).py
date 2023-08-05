import datetime
'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
 e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
'''
ano = int(input("Digite o ano de nascimento do atleta: "))
anoAtual = datetime.date.today().year
idade = anoAtual - ano
print(f"Idade do atleta: {idade}")

if idade <= 9:
    print("A categoria do atleta é: MIRIM")
elif idade <= 14:
    print("A categoria do atleta é: INFANTIL")
elif idade <= 19:
    print("A categoria do atleta é: JÚNIOR")
elif idade <= 25:
    print("A categoria do atleta é: SÊNIO")
else:
    print("A categoria do atleta é: MASTER")

