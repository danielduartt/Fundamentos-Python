'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''

valores = list()

while True:
    n = float(input("Digite um valor: "))
    if n in valores:
        print("Valor existente! ")
        print("Tente Novamente...")
    else:
        valores.append(n)
        print("Valore adicionado!")
    resp = input("Deseja Continuar[S/N]: ").strip().upper()
    if resp == 'N':
        print("Encerrando...")
        break
print(valores)
