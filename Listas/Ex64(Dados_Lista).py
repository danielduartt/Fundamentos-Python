'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''

lista = list()
while True:
    lista.append(int(input("Digite um valor: ")))
    resp = str(input("Quer continuar[S/N]: ")).strip()[0]
    if resp in 'Nn':
        print("Encerrando...")
        break
lista.sort()
print(f"A) Foram digitados {len(lista)} números\n"
      f"B) Lista na Ordem Crescente = {lista}")
lista.sort(reverse=True)
print(f"C) Lista na Ordem Decrescente = {lista}")
if 5 in lista:
    print("D) O 5 foi digitado na lista!", end='')
    print(f"/ Vezes: {lista.count(5)}")
else:
    print("D) O número 5 não foi digitado!")