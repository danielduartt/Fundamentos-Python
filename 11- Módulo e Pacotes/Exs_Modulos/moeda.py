'''
aumentar(), diminuir(), dobro() e metade()
'''

def aumentar(num):
    return num * 1.1

def diminuit(num):
    return num * 0.9

def dobro(num):
    return num * 2

def metade(num):
    return num / 2

def formatacao(valor = 0, moeda = 'R$'):
    return f"{moeda}{valor:.2f}".replace(',', '.')