#fatorial com while


num = int(input("Digite o número para calcular seu fatorial: "))
fatorial = 1

while num > 0:
    print(f"{num} ", end='')
    print('x ' if num > 1 else '= ', end='')
    fatorial *= num
    num -= 1
print(f"{fatorial}")
