import requests
from time import sleep
historic = dict()


def print_historic():
    for k, v in historic.items():
        print(f'{k} = {v}')
    print('-=' * 23)
    print('\033[0;36mObrigado por usar o programa, você é um amor <3\033[m')
    print('\033[0;36mPena que máquinas não sentem esse sentimento :D\033[m')
    print()
    print('\033[0;36mAté mais! <3\033[m ')

def titulo(txt):
    print('\033[0;33m-\033[m'*len(txt))
    print(txt)
    print('\033[0;33m-\033[m'*len(txt))
def op_moedas():
    titulo('1-USD \n2-EUR \n3-BTC')


def menu_conversor():
    titulo('CONVERSOR DE MOEDAS')
    titulo('-INSIRA O VALOR INICIAL EM REAIS PARA CAMBIAR\n-INSIRA PARA QUAL MOEDA DESEJA CAMBIAR')
    sleep(0.5)

def conversor(x,y):
    print()
    requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    requisicao_dic = requisicao.json()
    valor_dolar = float(requisicao_dic['USDBRL']['bid'])
    valor_euro = float(requisicao_dic['EURBRL']['bid'])
    valor_btc = float(requisicao_dic['BTCBRL']['bid'])
    if x == 'USD':
        dolar = y / valor_dolar
        print('\033[2;32m{} R$ equivale à {:.4f} US$\033[m'.format(y, dolar))
        historic['Resultado']= dolar
    elif x == 'EUR':
        euro = y / valor_euro
        print('\033[2;32m{} R$ equivale à {:.4f} €\033[m'.format(y, euro))
        historic['Resultado'] = euro
    elif x == 'BTC':
        bit = y / valor_btc
        print('\033[2;32m{} R$ equivale à {: .4f} ?\033[m'.format(y, bit))
        historic['Resultado'] = bit
    sleep(0.7)

def time_run(txt2):
    print('\033[0;36m'+txt2+'\033[m', end='')
    for x in range(0, 5):
        print('.', end='')
        sleep(0.4)
#programa
while True:
    menu_conversor()
    #valor inicial
    while True:
        try:
            titulo('VAlOR INICIAL:')
            sleep(0.5)
            valor_inicial= float(input('Insira o valor desejado(em reais): ').replace(',' , '.'))
            historic['Valor_inicial']= valor_inicial
            break
        except ValueError:
            print('\033[2;31mOpa! ocorreu um erro :(\033[m')
            print('\033[2;31mLembre-se de colocar um valor válido xD\033[m')
            sleep(0.5)
            print('\033[2;31mTente novamente\033[m')
    sleep(0.5)
    #moeda final
    titulo('SELECIONA A MOEDA PARA A CONVERSÃO:')
    op_moedas()
    sleep(0.5)
    moeda_final = 0
    while moeda_final not in (1,2,3):
        try:
            moeda_final = int(input('Insira a sua escolha: '))
            if moeda_final == 1:
                moeda_final = 'USD'
                historic['Moeda_de_cambio'] = moeda_final
                break
            elif moeda_final == 2:
                moeda_final = 'EUR'
                historic['Moeda_de_cambio'] = moeda_final
                break
            elif moeda_final == 3:
                moeda_final = 'BTC'
                historic['Moeda_de_cambio'] = moeda_final
                break
            else:
                print('\033[1;31mOpção inválida\033[m')
                print('\033[1;31mSelecione um valor de 1 a 3\033[m')
        except ValueError:
            print('\033[1;31mOpção inválida\033[m ')
            sleep(0.5)

    time_run( 'PROCESSANDO')
    conversor( moeda_final, valor_inicial)
    sleep(0.5)
    titulo('CONTINUAR?')
    resp=str(input('Deseja continuar?[S/N]:  '))
    sleep(0.5)
    if resp in 'Nn':
        print('-='*20)
        print('\033[1;31mEspere!\033[m')
        sleep(0.7)
        print('\033[1;31mAntes de sair...\033[m')
        print('-='*23)
        resp2=str(input('\033[0;36mDeseja acessar o histórico de suas ações? [S/N]\033[m'))
        print('-='*23)
        if resp2 in 'Ss':
            titulo('HISTÓRICO')
            print(historic)
            print_historic()
            break
        else:
            time_run('Já?! muito cedo! :( ')
            print()
            sleep(0.5)
            print('\033[0;36mNosso tempo juntos foi bom!\033[m')
            print()
            print('\033[0;36mTenha um bom dia <3\033[m')
            break