import time

def buscar_variavel_entrada():
    global variavel_entrada, linha_menor_elemento, coluna_pivo
    variavel_entrada = 1000
    linha_menor_elemento = 0
    coluna_pivo = 0

    output_file.write("\n\nProcurando Variável Que Entra:\n")
    time.sleep(4)

    for i in range(total_linhas):
        for j in range(total_colunas):
            if tabela[i][j] < variavel_entrada:
                variavel_entrada = tabela[i][j]
                linha_menor_elemento = i
                coluna_pivo = j

    output_file.write(f"Assim temos que a Variável que Entra é |{variavel_entrada}|\n")


def buscar_linha_pivo():
    global menor_pivo, linha_pivo, elemento_pivo
    menor_pivo = 1000
    linha_pivo = 0
    elemento_pivo = 0

    output_file.write("\nObtendo Linha Pivo:\n\n")
    time.sleep(5)

    for i in range(total_linhas):
        if i == linha_menor_elemento:
            continue
        if tabela[i][coluna_pivo] != 0:
            coluna_variavel_entrada = tabela[i][total_colunas - 1] / tabela[i][coluna_pivo]
            if coluna_variavel_entrada < menor_pivo and coluna_variavel_entrada > 0:
                menor_pivo = coluna_variavel_entrada
                linha_pivo = i
    elemento_pivo = tabela[linha_pivo][coluna_pivo]
    output_file.write(f"Linha Pivo: {linha_pivo}\n")
    output_file.write(f"\nElemento Pivo: {elemento_pivo}\n")


# Funções restantes...

if __name__ == "__main__":
    input_file = open("problema1.txt", "r")
    output_file = open("output.txt", "w")

    qtd_x, qtd_funcoes_limitantes, qtd_restricoes = map(int, input_file.readline().split())
    total_colunas = qtd_x + qtd_funcoes_limitantes + 2
    total_linhas = qtd_funcoes_limitantes + 1

    output_file.write("Informe os valores da tabela inicial formada linha a linha:\n")

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

        coeficientes.append(termo_independente)

        tabela.append(coeficientes)

    # Adicionando a função objetiva ao final da tabela
    funcao_objetiva.extend([0] * qtd_funcoes_limitantes)
    funcao_objetiva.append(0)

    tabela.append(funcao_objetiva)

    # Restante do código...

    input_file.close()
    output_file.close()
