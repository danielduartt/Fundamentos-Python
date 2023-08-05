'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
sair = False
while not sair:
    print("=-=" * 30)
    print("[ 1 ] somar")
    print("[ 2 ] multiplicar")
    print("[ 3 ] maior")
    print("[ 4 ] novos números")
    print("[ 5 ] sair do programa")
    print("=-=" * 30)
    resp = int(input("Resposta => "))
    if resp == 1:
        print(f"{n1} + {n2} = {n1 + n2}")
    elif resp == 2:
        print(f"{n1} * {n2} = {n1 * n2}")
    elif resp == 3:
        if n1 > n2:
            print(f"{n1} > {n2}")
        else:
            print(f"{n2} > {n1}")
    elif resp == 4:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
    elif resp == 5:
        print("Saindo do programa!")
        sair = True
    else:
        print("Opção inválida!")

