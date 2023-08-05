sexo = input("Informe seu sexo [M/F]: ").upper().strip()[0]
while sexo not in 'MmFf':
    sexo = input("Dados inválidos! Pfv informe seu sexo: ").upper().strip()[0]
print("Certo! opção válida")