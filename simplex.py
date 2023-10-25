def buscar_variavel_entrada():
    global variavel_entrada, linha_menor_elemento, coluna_pivo
    variavel_entrada = 1000
    linha_menor_elemento = 0
    coluna_pivo = 0

    for i_novo2 in range(total_linhas):
        for j in range(total_colunas):
            if tabela[i_novo2][j] < variavel_entrada:
                variavel_entrada = tabela[i_novo2][j]
                linha_menor_elemento = i_novo2
                coluna_pivo = j


def buscar_linha_pivo():
    global menor_pivo, linha_pivo, elemento_pivo
    menor_pivo = 1000
    linha_pivo = 0
    elemento_pivo = 0

    for i_novo in range(total_linhas):
        if i_novo == linha_menor_elemento:
            continue
        if tabela[i_novo][coluna_pivo] != 0:
            coluna_variavel_entrada = tabela[i_novo][total_colunas - 1] / tabela[i_novo][coluna_pivo]
            if menor_pivo > coluna_variavel_entrada > 0:
                menor_pivo = coluna_variavel_entrada
                linha_pivo = i_novo
    elemento_pivo = tabela[linha_pivo][coluna_pivo]


# Funções restantes...

if __name__ == "__main__":
    input_file = open("problema1.txt", "r")

    qtd_x, qtd_funcoes_limitantes, qtd_restricoes = map(int, input_file.readline().split())
    total_colunas = qtd_x + qtd_funcoes_limitantes + 2
    total_linhas = qtd_funcoes_limitantes + 1

    tabela = []

    # Lendo a função objetiva
    funcao_objetiva = list(map(float, input_file.readline().split()))

    # Lendo as restrições e adicionando as variáveis de folga e artificiais conforme necessário
    for i in range(qtd_funcoes_limitantes):
        restricao = input_file.readline().split()
        coeficientes = list(map(float, restricao[:-2]))
        sinal = None  # Define um valor padrão para 'sinal'
        termo_independente = None  # Define um valor padrão para 'termo_independente'
        if len(restricao) >= 2:
            sinal = restricao[-2]
        else:
            print(f"Formato de linha inesperado: {restricao}")
        if len(restricao) >= 1:
            termo_independente = float(restricao[-1])
            # Se o termo independente é negativo, multiplicamos toda a linha por -1
            if termo_independente < 0:
                coeficientes = [-coef for coef in coeficientes]
                termo_independente *= -1
        else:
            print(f"Formato de linha inesperado: {restricao}")

        # Adicionando as variáveis de folga e artificiais conforme necessário
        if sinal == "<=":
            coeficientes.extend([1] + [0] * (qtd_funcoes_limitantes - 1))
        elif sinal == "==":
            coeficientes.extend([0] * qtd_funcoes_limitantes)
        elif sinal == ">=":
            coeficientes.extend([-1] + [0] * (qtd_funcoes_limitantes - 1))
            coeficientes.append(1)  # Adiciona uma variável artificial

        coeficientes.append(termo_independente)

        tabela.append(coeficientes)

    # Adicionando a função objetiva ao final da tabela
    funcao_objetiva.extend([0] * qtd_funcoes_limitantes)

    # Se é um problema de maximização, multiplica a função objetivo por -1
    if qtd_restricoes == 1:
        funcao_objetiva = [-x for x in funcao_objetiva]

    funcao_objetiva.append(0)

    tabela.append(funcao_objetiva)

    # Restante do código...

    input_file.close()
