'''
Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma
mensagem com tamanho adaptável.
'''

def PrintDiferente(msg):
    tamanho = len(msg) + 6
    print("~"*tamanho)
    metade = int(len(msg)/2)
    print(f"   {msg}")
    print("~" * tamanho)

PrintDiferente("Teste")