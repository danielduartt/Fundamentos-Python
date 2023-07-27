'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''
from datetime import date
trabalhador = dict()

trabalhador['nome'] = input("Digite o nome do trabalhador: ")

nascimento = int(input("Digite o ano de nascimento dele: "))
hoje = date.today().year
idade = hoje - nascimento
trabalhador['idade'] = idade

ctps = int(input("Digite o número da carteira de trabalho (0 caso não tenha): "))
trabalhador['CTPS'] = ctps

if trabalhador['CTPS'] != 0:
    anoContratacao = int(input("Digite o ano de contratação: "))
    trabalhador['Salário'] = float(input("Digite o salário: "))
    trabalhador['Aposentadoria'] = anoContratacao + 50
    print(f"- Nome: {trabalhador['nome']}")
    print(f"- Idade: {trabalhador['idade']}")
    print(f"- CTPS: {trabalhador['CTPS']}")
    print(f"- Salario: {trabalhador['Salário']}")
    print(f"- Aposentadoria: {trabalhador['Aposentadoria']}")
else:
    print(f"- Nome: {trabalhador['nome']}")
    print(f"- Idade: {trabalhador['idade']}")
    print(f"- CTPS: {trabalhador['CTPS']}")





