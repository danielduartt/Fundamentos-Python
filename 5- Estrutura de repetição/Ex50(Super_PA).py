'''
Perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.
'''
print("=-=-=-=-=-=-=-=-=")
print("  Gerador de PA  ")
print("=-=-=-=-=-=-=-=-=")
p1 = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
total = 0
mais = 10
cont = 1
while mais != 0:
    total += mais
    while cont <= total:
        print(f"{p1} ", end='')
        print(" + " if cont < 10 else ' -> ', end ='')
        cont += 1
    print("PAUSE")
    mais = int(input("Quantos termos você quer a mais: "))
print("FIM")