'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''

palavras = ('feijao', 'coxinha', 'emprego', 'namorada',
            'conhecimento', 'estagio', 'dinheiro', 'felicidade'
            , 'data science', 'progamar')
for c in palavras:
    print(f"\nEm {c.upper()} temos: ", end = '')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(f"{letra}", end='')