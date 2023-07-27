'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''

numeros = list()
par = list()
impar = list()

while True:
    c = int(input("Digite um número: "))
    numeros.append(c)
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)

    resp = input("Deseja Continuar[S/N]: ").strip().upper()[0]
    if resp == "N":
        print("Encerrando...")
        break
print(f"Lista digitada: {numeros}")
print(f"Pares: {par}\nImpares: {impar}")
