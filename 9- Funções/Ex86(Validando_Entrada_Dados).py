'''
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')
'''


def leiaInt(frase):
    while True:
        valor = input(frase).strip()
        if valor.isnumeric():
            return valor
            break
        else:
            print("ERRO! VALOR NÃO NUMÉRICO!")


n = leiaInt("Digite um número: ")
print(f"Voce acabou de digitar o número {n}")