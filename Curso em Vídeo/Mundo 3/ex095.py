"""
Aprimore o DESAFIO 093 para que ele funcione  com vários jogadores, incluindo um sistema de visualização
de detalhes do aproveitamento de cada jogador.
"""
cadastro = dict()
dados = list()
gols = list()
while True:
    total = 0
    cadastro["Nome"] = str(input("Nome do Jogador: ")).title().strip()
    partidas = int(input(f"Quantas partidas {cadastro['Nome']} jogou? R:"))
    for x in range(0, partidas):
        gols.append(int(input(f"Quantos gols na partida {x+1}? R:")))
        total += gols[x]
    cadastro["Gols"] = gols[:]
    cadastro["Total"] = total
    dados.append(cadastro.copy())
    gols.clear()
    cadastro.clear()
    stop = ""
    while (stop != "S") and (stop != "N"):
        stop = str(input("Você deseja continuar? [S/N]:")).upper().strip()
    if stop == "N":
        print("-=-" * 20)
        break
    print("-=-"*20)
print(f"{'Nº:':<4}{'Nome:':<15}{'Total:':<8}{'Gols:'}")
for x in range(0, len(dados)):
    print(f"{x:<4}{dados[x]['Nome']:<16}{dados[x]['Total']:<8}{dados[x]['Gols']}")
print("-=-"*20)
escolha = 0
while escolha != 999:
    escolha = int(input("Mostrar dados de qual jogador? (999 para parar):"))
    if escolha != 999:
        if (escolha < 0) or (escolha >= len(dados)):
            print(f"ERRO! Não existe jogador com código {escolha}! Tente novamente...")
        else:
            print(f"-- LEVANTAMENTO DO JOGADOR {dados[escolha]['Nome']}:")
            for x, y in enumerate(dados[escolha]['Gols']):
                print(f"No jogo {x+1} fez {y} gols.")
        print("-=-"*20)
    else:
        print("VOLTE SEMPRE!")
