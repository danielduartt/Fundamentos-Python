
#Crie um programa que leia dis números e imprima qual é o maior
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))


if n1 > n2 and n1 > n3:
    print("O {} é o maior número!".format(n1))
    maior = n1
elif n2 > n1 and n2 > n3:
    print("O {} é o maior número!".format(n2))
    maior = n2
else:
    maior = n3
    print("O {} é o maior número!".format(n3))


'''
if n1 > n2:
    print(f"{n1} é maior que {n2}")
else:
    print(f"{n1} é menor que {n2}")
'''