'''
 Melhore o jogo do DESAFIO  onde o computador vai "pensar"
 em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
 mostrando no final quantos palpites foram necessários para vencer.
'''
from random import randint
print("SOU SEU COMPUTADOR.....")
print("Acabei de pensar em um número de 0 e 10!\nTente adivinhar qual foi")
print("Será que você consegue? ")
computador = randint(0, 10)

acertou = False
while not acertou:
    player = int(input("Qual o seu palpite? => "))
    if player == computador:
        print(f"A máquina escolheu {computador}")
        print("Você acertou! ")
        acertou = True
    else:
        print(f"Não foi dessa vez! a máquina escolheu {computador}")
