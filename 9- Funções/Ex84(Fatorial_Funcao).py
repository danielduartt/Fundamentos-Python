'''
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show,
que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
'''


def fatorial(num, show=0):
    """
    num = numero que deseja calcular o fatorial
    show = (0 = não mostrar, 1 = mostrar)
    """
    fat = 1
    if show == 1:
        for i in range(num, 0, -1):
            print(f" {i} ", end='')
            if i > 1:
                print(" x ", end='')
            else:
                print(" = ", end='')
            fat *= i
        print(f"{fat}", end='')
    else:
        for i in range(num, 1, -1):
            fat *= i
        print("\nO valor do fatorial é {}".format(fat))

fatorial(3)

fatorial(3, 1)
