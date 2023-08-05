'''
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual
foi o maior e o menor valores lidos. O programa deve perguntar ao
usuário se ele quer ou não continuar a digitar valores.
'''

resp = 'S'
num = maior = menor = count = soma = 0
while resp in 'Ss':
    num=int(input("Digite um número: "))
    soma += num
    count += 1
    if count == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = input("Deseja continuar[S,N]: ")
media = soma / count
print(f"Maior: {maior}\nMenor: {menor}\nMédia: {media}")

