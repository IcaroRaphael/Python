"""
Código ANSI: \033[style;text;backm
Exemplo: \033[0;33;44m

STYLE:
0 = None
1 = Negrito
4 = Sublinhado
7 = Inverte Letra/Fundo

TEXT:
30 = Branco
31 = Vermelho
32 = Verde
33 = Amarelo
34 = Azul
35 = Rosa
36 = Ciano
37 = Cinza

BACK(Background):
40 = Branco
41 = Vermelho
42 = Verde
43 = Amarelo
44 = Azul
45 = Rosa
46 = Ciano
47 = Cinza
"""
print("\033[7;33;44mOlá, Mundo!\033[m")

a = 3
b = 5
print("Os valores são \033[32m{}\033[m e \033[31m{}\033[m".format(a, b))

nome = "Ícaro"
print("Olá, muito prazer em te conhecer {}{}{}!!!!".format("\033[34m", nome, "\033[m"))

cores = {"limpa":"\033[m", "azul":"\033[34m", "amarelo":"\033[33m", "pretoebranco":"/033[7;30m]"}
print("{}Olá{}, {}mundo!{}".format(cores["amarelo"], cores["limpa"], cores["azul"], cores["limpa"]))
