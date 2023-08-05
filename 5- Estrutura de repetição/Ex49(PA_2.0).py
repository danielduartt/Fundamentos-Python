print("=-=-=-=-=-=-=-=-=")
print("  Gerador de PA  ")
print("=-=-=-=-=-=-=-=-=")
p1 = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
cont = 1
somatorio = 0
while cont <= 10:
    print(f"{p1} ", end='')
    print(" + " if cont < 10 else ' = ', end ='')
    p1 += razao
    cont += 1