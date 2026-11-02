def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    for i in range(tamanho):
        if orientacao == "vertical":
            posicoes.append([linha + i, coluna])
        else:
            posicoes.append([linha, coluna + i])
    return posicoes

def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    for i in range(tamanho):
        if orientacao == 'vertical':
            posicoes.append([linha + i, coluna])
        elif orientacao == 'horizontal':
            posicoes.append([linha, coluna + i])
    return posicoes
def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio not in frota:
        frota[nome_navio] = []
    frota[nome_navio].append(posicoes)
    return frota 

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'     
    else:
        tabuleiro[linha][coluna] = '-'     
    return tabuleiro 

def posiciona_frota(frota):
    tabuleiro = []
    for i in range(10):
        tabuleiro.append([0] * 10)
    for navio in frota:
        for embarcacao in frota[navio]:
            for posicao in embarcacao:
                linha = posicao[0]
                coluna = posicao[1]
                tabuleiro[linha][coluna] = 1
    return tabuleiro

def afundados(frota,tabuleiro):
    total = 0
    for tipo,navios in frota.items():
        for navio in navios:
            atingidos = 0
            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]
                if tabuleiro[linha][coluna] == 'X':
                    atingidos += 1
            if atingidos == len(navio):
                total += 1
    return total

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    for posicao in posicoes:
        if posicao[0] < 0 or posicao[0] > 9:
            return False
        if posicao[1] < 0 or posicao[1] > 9:
            return False
        for navio in frota:
            for embarcacao in frota[navio]:
                if posicao in embarcacao:
                    return False
    return True

frota = {}
navios = {'porta-avioes': [4,1], 'navio-tanque': [3,2], 'contratorpedeiro': [2,3], 'submarino': [1,4] } 
for navio in navios:
    tamanho = navios[navio][0]
    quantidade = navios[navio][1]
    for i in range(quantidade):
        print(f'Insira as informações referentes ao navio {navio} que possui tamanho {tamanho}')
        valido = False
        while not valido:
            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))
            if navio == 'submarino':
                orientacao = 'horizontal'
            else:
                escolha = int(input('[1] Vertical [2] Horizontal > '))
                if escolha == 1:
                    orientacao = 'vertical'
                else:
                    orientacao = 'horizontal'
            valido = posicao_valida(frota, linha, coluna, orientacao, tamanho)
            if not valido:
                print('Esta posição não está válida!')
        frota = preenche_frota(frota, navio, linha, coluna, orientacao, tamanho)
print(frota)