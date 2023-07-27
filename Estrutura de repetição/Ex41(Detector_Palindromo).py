#Crie um programa que leia uma frase qualquer
# e diga se ela é um palíndromo, desconsiderando os espaços.

frase = input("Digite uma frase: ").upper().strip()
frase = frase.split()
frase = ''.join(frase)
inverso = ''
print(frase)
print("O inverso de {} é ".format(frase), end = ' ')
for i in range(len(frase) - 1, - 1, -1):
    inverso += frase[i]
    print(frase[i], end = '')
if frase == inverso:
    print("\nO nome digitado é um palíndromo")
else:
    print("O nome digitado não é um palíndromo")
