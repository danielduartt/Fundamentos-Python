tuplas = ("Lápis", 1.75,
          "Borracha", 2.5,
          "Caderno", 14.5,
          "Estojo", 17,
          "Mochila",90)
print("-"*30)
print(f"{'Listagem de Produtos':^30}")
print("-"*30)
for c in range(0, len(tuplas)):
    if c % 2 == 0:
        print(f"{tuplas[c]:.<20}", end = '')
    else:
        print(f"R${tuplas[c]:>7.2f}")
print("-"*30)