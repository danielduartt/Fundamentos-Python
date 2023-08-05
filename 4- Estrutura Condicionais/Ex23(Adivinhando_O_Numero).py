import random
print("=-="*20)
nome = "Tente acertar o número entre 0 e 5 escolhido pelo computador!"
print(nome)
print("=-="*20)
num = random.randint(0, 6)
numEsc = int(input("Digite o número escolhido: "))
print(num)
if numEsc == num:
    print("Parabéns! Você acertou!")
else:
    print("Infelizmente não foi dessa vez, tente mais tarde")