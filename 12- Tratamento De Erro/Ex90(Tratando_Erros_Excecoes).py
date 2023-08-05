'''
Função aprofundada
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade
da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat()
com a mesma funcionalidade.
'''



def leiaInt(frase):
    while True:
        try:
            valor = int(input(f"{frase}"))
        except (ValueError, TypeError):
            print("ERRO! NÚMERO INVÁLIDO")
            continue
        else:
            return valor #da um break

def leiaFloat(frase):
    while True:
        try:
            valor = float(input(f"{frase}"))
        except (ValueError, TypeError):
            print("ERRO! NÚMERO INVÁLIDO")
            continue
        else:
            return valor

n = leiaInt("Digite um número inteiro: ")
print(n)

m = leiaFloat("Digite um número float: ")
print(m)


