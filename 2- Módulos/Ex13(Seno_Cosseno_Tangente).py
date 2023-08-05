#crie um programa que calcule o seno, cosseno e tangente
import math
angulo = float(input("Digite o angulo que você deseja: "))#graus
#tem que ta em radianos
print(f"Seno: {math.sin(math.radians(angulo))}\n"
      f"Cosseno: {math.cos(math.radians(angulo))}\n"
      f"Tagente: {math.tan(math.radians(angulo))}")