'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos
e fechados na ordem correta.
'''
exp = input("Digite a expressão: ")
pilha = list() #primeiro a entrar, ultimo a sair
count = 0
for c in exp:
    if c == "(":
        pilha.append('(') #empilha
        count += 1
    elif c == ")":
        count -= 1
        if len(pilha) > 0:
            pilha.pop() #desempilha
        else:
            pilha.append(")") #empilha
            break
print("~"*20)
if len(pilha) == 0:
    print("Expressão válida!")
else:
    print("Expressão iválida!")
print("~"*20)
