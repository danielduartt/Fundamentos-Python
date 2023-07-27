'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
'''

peso = int(input("Digite seu peso: "))
altura = str(input("Digite sua altura: ")).replace(',', '.')
altura = float(altura)
IMC = peso / (altura**2)
print("Seu imc é {:.2f}!".format(IMC))

if IMC > 18.5 and IMC <= 25:
    print("Peso Ideal")
elif IMC <= 30:
    print("Sobrepeso")
elif IMC <= 40:
    print("Obesidade")
else:
    print("Thais carla")

