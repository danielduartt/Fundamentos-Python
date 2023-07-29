str = input('Digite a string:')
x = 0
lista = []
while x < len(str):
    if str[x] == '[':
        lista.append('[')
    if str[x] == ']':
        if len(lista) > 0:
            topo = lista.pop(-1)
        else:
            lista.append(']')
            break
    x = x + 1
if len(lista) == 0:
    print('certa')
else:
    print('errada')