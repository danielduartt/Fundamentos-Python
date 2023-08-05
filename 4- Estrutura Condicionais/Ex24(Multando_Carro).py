'''
Escreva um programa que leia a velocidade de um carro e imprima na tela se foi ultado ou não
aplicando 7 reais a cada km a mais do limite de velocidade
'''
vel = float(input("Digite a velocidade do carro: "))

if(vel <= 80):
    print("Não mutado, velociade abaixo do limite")
else:
    valor = (vel - 80) * 7
    print("MUTADO!!!!\nMulta aplicada de {} reais".format(valor))
print("Tenha um Bom Dia, e dirija com segurança!")