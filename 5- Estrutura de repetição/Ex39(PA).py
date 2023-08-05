#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
print("==========================")
print('   10 TERMOS DE UMA PA      ')
print("==========================")
p1 = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
ultimoTermo = p1 + (10-1)*razao
soma = 0
for c in range(p1 , ultimoTermo + razao, razao):
    print(f"{c}", end=" -> ")
    soma += c
print("*Resultado = {}".format(soma))
