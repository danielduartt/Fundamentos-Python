'''
Faça um programa que tenha uma função chamada área(), que receba as dimensões
de um terreno retangular (largura e comprimento) e mostre a área do terreno.
'''


def Area(largura, comprimento):
    return largura * comprimento


a = float(input("Digite a largura(m): "))
b = float(input("Digite o comprimento(m): "))
res = Area(a, b)
print(f"A área é: {res} m²")
