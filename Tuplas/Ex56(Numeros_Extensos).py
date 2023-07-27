'''
 Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
 Seu programa deverá ler um número pelo teclado (entre 0 e 10) e mostrá-lo por extenso.
'''

numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
numeroEsc = int(input("Digite um número de 0 a 10: "))
print(f"O número por extenso é {numeros[numeroEsc]}")
