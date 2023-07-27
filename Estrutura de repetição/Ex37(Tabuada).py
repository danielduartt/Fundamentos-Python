#crie um programa que receba um numero e calcule sua tabuada usando for

num = int(input("Digite o número para saber sua tabuada: "))
print("TABUADA DE {}".format(num))
for i in range(1,11):
    print("{} x {} = {}".format(num, i, num*i))