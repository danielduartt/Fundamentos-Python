
#crie um programa que receba uma número real e imprima a porção inteira dele
from math import trunc
num = float(input("Digite um valor: "))

print("---------------------Primeira Forma-----------------------")
print(f"O número digitado foi {num}, sua porção inteira é {int(num)}")
print("---------------------Segunda Forma--------------------------")
print(f"O número digitado foi {num}, sua porção inteira é {trunc(num)}")