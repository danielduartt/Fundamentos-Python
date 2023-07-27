'''
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.
'''

principal = [[], []]

for c in range(1, 8):
    n = int(input(f"Digite o {c} número: "))
    if n % 2 == 0:
        principal[0].append(n)
    else:
        principal[1].append(n)

principal[0].sort()
principal[1].sort()
print(f"Par: {principal[0]}\nImpar: {principal[1]}")

