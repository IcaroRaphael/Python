"""
Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.
"""
import urllib
import urllib.request

try:
    site = urllib.request.urlopen("http://www.pudim.com.br")
except urllib.error.URLError:
    print("\033[31mO site \033[4mPudim.com.br\033[m\033[31m não está acessível no momento.\033[m")
else:
    print("\033[32mO site \033[4mPudim.com.br\033[m\033[32m está acessível no momento.\033[m")
