'''
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha
'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
soma2 = 0
maior = menor = 0

for l in range(0, 3):
    for c in range(0, 3):
        n = int(input(f"[{l},{c}]: "))
        matriz[l][c] = n
        if n % 2 == 0:
            soma += n

print("~"*20)
print(f"{'Matriz':^20}")
print("~"*20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"{matriz[l][c]:^5}", end='')
    print()
print("~"*20)

for l in range(0, 3):
    soma2 += matriz[l][2]
for c in range(0, 3):
    n = matriz[1][c]
    if n > maior:
        maior = n
print(f"A) Soma dos valores pares: {soma}")
print(f"B) Soma da terceira coluna: {soma2}")
print(f"C) Maior valor da segunda linha: {maior}")



