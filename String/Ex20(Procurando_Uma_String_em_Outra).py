#crie um programa que ache qualquer string dentro deu um texto
texto = input("Digite um texto: ").strip().lower()
nome = input("Digite uma string para ver se está dentro do texto: ").lower()
if(nome in texto):
    print(f"{nome} está no texto")
else:
    print(f"{nome} não está no texto")

