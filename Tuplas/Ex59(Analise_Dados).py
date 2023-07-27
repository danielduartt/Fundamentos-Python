'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''
n1 = int(input("Digite um número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro  número: "))
n4 = int(input("Digite o quarto número: "))
numeros = (n1, n2, n3, n4)
existe = False
print(f"O número 9 aparece {numeros.count(9)}")
for i in numeros:
    if i == 3:
        existe = True
if existe:
    print(f"A posição do 3 é {numeros.index(3)}")

print("Números Pares: (", end = ' ')
for i in numeros:
    if i % 2 == 0:
       print(f"{i}", end= ' ')
print(")")







