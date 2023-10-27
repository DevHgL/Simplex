import numpy as np

def resolve(tableau, otimizacao):
    best_i = -1
    exit_val_i = -1
    while True:
        fo = np.delete(tableau[0], np.where(tableau[0] == 0))
        
        # TODO Considere verificar se tem que fazer tratativa pra max e min ou se tem como só jogar todo problema de max pra mim ou vice versa
        if otimizacao: best = np.amax(fo)
        else: best = np.amin(fo)

        
        # Interrompendo se não houverem valores negativos na minimização
        if not otimizacao and best > 0: break
        # Interrompendo se não houverem valores positivos na maximização
        if otimizacao and best < 0: break

        # Selecionando a Variável de Entrada
        best_i = np.where(fo == best)[0][0]

        # Interrompendo se o valor de melhora for o mesmo que foi removido anteriormente
        if best_i == exit_val_i: break

        #Selecionando a Coluna Pivô
        pivot_column = tableau[:,best_i]
        
        b = tableau[:,-1]
        b_results = b/pivot_column
        b_results = np.delete(b_results, np.where(b_results <= 0))

        if len(b_results) == 0: break

        # Selecionando a Variável de Saída
        exit_val = np.amin(b_results)
        exit_val_i = np.where(b_results == exit_val)[0][0] + 1
        
        # Transformando em Identidade
        # Dividindo a linha da variável de Entrada para
        tableau[exit_val_i] = tableau[exit_val_i]/tableau[exit_val_i][best_i]

        # Transformações lineares
        for row_i in range(len(tableau)):
            if (row_i != exit_val_i):
                pivot = tableau[row_i][best_i]
                row = -pivot * tableau[exit_val_i]
                tableau[row_i] = tableau[row_i] + row
        
        tableau = np.around(tableau, 2)

    return tableau[:,-1]