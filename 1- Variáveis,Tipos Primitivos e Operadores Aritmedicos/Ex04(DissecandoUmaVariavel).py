variavel = (input("Digite algo: ")) #toda função input retorna uma string
print("Tipo = {}".format(type(variavel))) #poderia ser "Tipo = " , type(variavel)
print("Só tem espaços = ", variavel.isspace()) #É só espaços? [true/false]
print("É um número = ", variavel.isnumeric())
print("É alfabético = ", variavel.isalpha()) #É alfabético? Só letras
print("É alfaNumérico = ", variavel.isalnum()) #É alfanumérico? Letras e Números?
print("Maiúsculo = ", variavel.isupper())# Só Maiuscula?
print("Minúscula = ", variavel.islower())#Só Minúscula?
print("Capitalizada = ", variavel.istitle())#Capitalizada = Começa com letra Maiúscula?
