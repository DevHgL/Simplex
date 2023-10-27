import numpy as np

def criar_tableau(coeficientes_funcao_objetivo, coeficientes_restricoes, termos_independentes, otimizacao, operations):
    num_restricoes = len(coeficientes_restricoes)
    num_variaveis = len(coeficientes_funcao_objetivo)

    tableau = np.zeros((num_restricoes + 1, num_variaveis + num_restricoes + 1))

    # Configurar a função objetivo na primeira linha do tableau
    tableau[0, :num_variaveis] = coeficientes_funcao_objetivo

    for i in range(num_restricoes):
        if termos_independentes[i] < 0:
            tableau[0] = -tableau[0]
            termos_independentes = -termos_independentes
            if operations[i] == "<=":
                operations[i] = ">="
            elif operations[i] == ">=":
                operations[i] = "<="

    # Configurar as restrições e os termos independentes
    for i in range(num_restricoes):
        tableau[i + 1, :num_variaveis] = coeficientes_restricoes[i]
        tableau[i + 1, num_variaveis + i] = 1 if operations[i] == '<=' or operations[i] == '==' else -1  # Adicionando variáveis de folga
        tableau[i + 1, -1] = termos_independentes[i]

    return tableau