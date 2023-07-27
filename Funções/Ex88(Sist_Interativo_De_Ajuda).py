'''
Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
'''

c = ('\033[m', '\033[0;30;41m')
def helpInterativo():
    from time import sleep
    msg = 'SISTEMA DE AJUDA PYHELP'
    while True:
        print("~" * (len(msg) + 4))
        print(f"  {msg}")
        print("~" * (len(msg) + 4))
        funcBiblio = input("Função ou Biblioteca >>> ").strip()
        if funcBiblio.lower() == 'fim':
            print("Encerrando")
            break
        else:
            print("~" * 40)
            print(f"  Acessando o manual do comando {funcBiblio}")
            print("~" * 40)
            sleep(1)
            help(funcBiblio)


helpInterativo()