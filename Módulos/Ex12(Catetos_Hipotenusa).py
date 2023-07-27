

#crie um programa que receba o valor do cateto oposto e do adjacente e calcule a hipotenusa
import math
op = float(input("Digite o valor do cateto oposto: "))
ad = float(input("Digite o valor do cateto adjacente: "))
soma = (op**2) + (ad**2)
hip = math.sqrt(soma)
print("O valor da hipotenusa será: {}".format(hip))

print("---------------------OUTRA FORMA---------------------")
hip2 = math.hypot(op,ad)
print("Outro método: {}".format(hip2))