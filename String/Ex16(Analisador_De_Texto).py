
#Analisaor de Texto

nome = str(input("Digite seu nome: ")).strip()
print("Seu nome em maiúculo: {}".format(nome.upper()))
print("Seu nome em minúsculo: {}".format(nome.lower()))
print(f"Seu nome tem {len(nome) - nome.count(' ')} letras ")
separa = nome.split()
print("Seu primeiro é nome {} e tem {} letras".format(separa[0],nome.find(' ')))