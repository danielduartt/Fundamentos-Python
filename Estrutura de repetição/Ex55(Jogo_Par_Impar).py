'''
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''
import random

while True:
    print("=-="*8)
    EscPlayer = input("Digite sua escolha[P/I]: ").strip().upper()
    EscComp = "P" if EscPlayer == "I" else "I"
    NumPlayer = int(input("Digite seu número[1-5]: "))
    NumComp = random.randint(1, 5)
    vitoria = 0
    soma = NumComp + NumPlayer
    print(f"A máquina escolheu {NumComp}!")
    print(f"A soma Deu {soma}")
    print(f"Logo..........")
    print("~" * 35)
    if soma % 2 == 0:
        if EscPlayer == 'P':
            print("Vc ganhou!!")
            vitoria += 1
        else:
            print("A máquina Ganhou :/")
    else:
        if EscPlayer == 'I':
            print("Vc ganhou!!")
            vitoria += 1
        else:
            print("A máquina Ganhou :/")
    print("~" * 35)
    resp = input("Deseja ir outra vez[S/N]: ").strip().upper()
    if resp == 'N':
        break

print(f"Vc ganhou {vitoria} ", end='')
print("vez!" if vitoria == 1 else "vezes!")


