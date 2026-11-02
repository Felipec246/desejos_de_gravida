from funcoes import preenche_frota, define_posicoes, posicao_valida

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

print(frota)