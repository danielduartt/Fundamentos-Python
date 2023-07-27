'''
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''
temp = []
princ = []
maior = menor = 0
while True:
    temp.append(input("Digite o Nome da pessoa: "))
    temp.append(float(input("Digite o Peso dela: ")))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    rep = input("Deseja continuar[S/N]: ").strip().upper()[0]
    if rep == 'N':
        print("Encerrando...")
        break

print(f"Os dados foram {princ}")
print(f"A) Pessoas cadastradas: {len(princ)}")
print(f"B) Maior peso foi: {maior}Kg, Peso de ", end='')
for p in princ:
    if p[1] == maior:
        print(f"{p[0]} ", end='')
print(f"\nC) Menor peso foi: {menor}Kg, Peso de ", end='')
for a in princ:
    if a[1] == menor:
        print(f"{p[0]}", end='')

