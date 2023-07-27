#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
opcoes = ['papel', 'tesoura', 'pedra']
computador = opcoes[randint(0, 4)]
print("-"*40)
print("PEDRA,PAPEL OU TESOURA? ")
print("-"*40)
sleep(0.5)
player = input("Digite sua escola: ").lower()
sleep(0.75)
print("JO")
sleep(0.75)
print("KEN")
sleep(0.75)
print("PO!!!!")
sleep(1)
print("=-="*20)
print("O computador escolheu {} ".format(computador))
if player == computador:
    print("Empatou! tente dnv!")
elif player == "tesoura" and computador == "pedra":
    print("Perdeu pra máquina, mané!")
elif player == 'pedra' and computador == 'tesoura':
    print("Parabéns! Você ganhou! ")
elif player == 'papel' and computador == 'tesoura':
    print("Perdeu pra máquina, mané!")
elif player == 'tesoura' and computador == 'papel':
    print("Parabéns! Você ganhou! ")
elif player == "pedra" and computador == "papel":
    print("Perdeu pra máquina, mané!")
elif player == "papel" and computador == "pedra":
    print("Parabéns! Você ganhou! ")
print("=-="*20)

