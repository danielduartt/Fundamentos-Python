'''
Função lambda = Função anônima, não tem o def

'''

def calcular_imposto(preco):
    return preco * 0.3

preco = 500
calcular_preco1 = calcular_imposto(preco)
calcular_imposto2 = lambda preco: preco * 0.3 #recebe um valor (:) vai dá a resposta


precos = [100, 500, 10, 25]

#o map aplica uma função em todos os valores de uma lista
impostos = list(map(lambda x: x * 0.3, precos))#to dizendo pra passar os valores de precos, na função atrás delas
                                                # nesse caso é a função lambda
                                                