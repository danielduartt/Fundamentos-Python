'''
Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo. Seu programa tem que
realizar três contagens através da função criada:
'''

def contador(ini, fim, passo):
    print(f"***** De {ini} até {fim} em {passo} em {passo} *****")
    if ini < fim and passo > 0:
        for i in range(ini, fim + 1, passo):
            print(f"{i}", end=' ')
    elif ini > fim and passo < 0:
        for i in range(ini, fim - 1, passo):
            print(f"{i}", end=' ')
    else:
        print("ERRO!")

#testando
contador(30, 15, -1)
print("\n-----------------------------")
contador(0, 20, 2)
print("\n-----------------------------")
contador(100, 20, -4)
