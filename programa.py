from funcoes import preenche_frota, define_posicoes, posicao_valida, posiciona_frota, faz_jogada, afundados
import random
frota = {}

navios = {
    'porta-aviões': [4, 1],
    'navio-tanque': [3, 2],
    'contratorpedeiro': [2, 3],
    'submarino': [1, 4]
}

for navio in navios:
    tamanho = navios[navio][0]
    quantidade = navios[navio][1]

    for i in range(quantidade):
        valido = False

        while not valido:
            print(f'Insira as informações referentes ao navio {navio} que possui tamanho {tamanho}')

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

            valido = posicao_valida(
                frota, linha, coluna, orientacao, tamanho
            )

            if not valido:
                print('Esta posição não está válida!')

        frota = preenche_frota(
            frota, navio, linha, coluna, orientacao, tamanho
        )


def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto
frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_jogador = posiciona_frota(frota)
tabuleiro_oponente = posiciona_frota(frota_oponente)

jogando = True
posicoes_atacadas = []
posicoes_atacadas_oponente = []

while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    posicao_inedita = False

    while not posicao_inedita:
        linha = int(input('Jogador, qual linha deseja atacar? '))

        while linha < 0 or linha > 9:
            print('Linha inválida!')
            linha = int(input('Jogador, qual linha deseja atacar? '))

        coluna = int(input('Jogador, qual coluna deseja atacar? '))

        while coluna < 0 or coluna > 9:
            print('Coluna inválida!')
            coluna = int(input('Jogador, qual coluna deseja atacar? '))

        if [linha, coluna] in posicoes_atacadas:
            print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')
        else:
            posicao_inedita = True

    posicoes_atacadas.append([linha, coluna])

    tabuleiro_oponente = faz_jogada(
        tabuleiro_oponente, linha, coluna
    )

    total_afundados = afundados(
        frota_oponente, tabuleiro_oponente
    )

    if total_afundados == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False

    if jogando:
        linha_oponente = random.randint(0, 9)
        coluna_oponente = random.randint(0, 9)

        while [linha_oponente, coluna_oponente] in posicoes_atacadas_oponente:
            linha_oponente = random.randint(0, 9)
            coluna_oponente = random.randint(0, 9)

        posicoes_atacadas_oponente.append([linha_oponente, coluna_oponente])

        print(f'Seu oponente está atacando na linha {linha_oponente} e coluna {coluna_oponente}')

        tabuleiro_jogador = faz_jogada(
            tabuleiro_jogador, linha_oponente, coluna_oponente
        )

        total_afundados_jogador = afundados(
            frota, tabuleiro_jogador
        )

        if total_afundados_jogador == 10:
            print('Xi! O oponente derrubou toda a sua frota =(')
            jogando = False