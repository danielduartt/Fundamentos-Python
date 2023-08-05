
import math
'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''

valor = float(input("Digite o valor da casa: "))
salario = float(input("Digite o valor do salário: "))
anos = float(input("Digite em quantos anos você deseja pagar: "))

meses = anos * 12
prestacao = valor/meses
print("A prestação será de {}".format(prestacao))
if prestacao >= salario * 0.3:
    print("Impréstimo negado!!")
else:
    print("Impréstimo aceito!!")
