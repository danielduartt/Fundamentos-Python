#crie um programa que calcule o valor da passagem para viagens curtas e longas
#viagem curta = 0.5 por km
#viagem longa = 0.45 por km

DistViagem = float(input("Digite a distância da viagem: "))
if DistViagem <= 200:
    valor = DistViagem * 0.5
    print("Valor da passagem: {:.2f}". format(valor))
else:
    valor = DistViagem * 0.45
    print("Valor da passagem: {:.2f}".format(valor))