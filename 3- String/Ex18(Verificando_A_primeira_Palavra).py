city = input("Digite a cidade que você nasceu: ").upper().strip()
print("Se começar com 'Santos', o resultado será true")
separacao = city.split()
print("SANTOS" in separacao[0])
