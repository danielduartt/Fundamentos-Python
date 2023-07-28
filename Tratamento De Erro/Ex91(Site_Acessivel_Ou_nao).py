'''
Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
'''

import urllib
import urllib.request
try:
    site = urllib.request.urlopen("https://www.instagram.com/")
except:
    print("O site bão está acessível no momento!")
else:
    print("Consegui acessar o síte!")

    