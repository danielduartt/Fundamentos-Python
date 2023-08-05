
#crie um programa que receba uma string e mostre quantas letras a tem nela, a posição a primeira e a posição da ultima
nome = input("Digite seu nome completo: ").strip().lower()
print(f"A letra 'a' aparece {nome.count('a')}" )
print(f"A primeira letra 'a' aparece {nome.find('a') + 1}")
print(f"A última letra 'a' aparece na posição {nome.rfind('a') + 1}")