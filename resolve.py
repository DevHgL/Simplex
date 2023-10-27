import numpy as np

def simplex_algorithm(tableau, optimization_type):
    entering_variable_index = -1
    exiting_variable_index = -1
    while True:
        objective_coefficients = np.delete(tableau[0], np.where(tableau[0] == 0))

        if optimization_type:
            best_coefficient = np.amax(objective_coefficients)
        else:
            best_coefficient = np.amin(objective_coefficients)

        if not optimization_type and best_coefficient > 0:
            break
        if optimization_type and best_coefficient < 0:
            break

        entering_variable_index = np.where(objective_coefficients == best_coefficient)[0][0]

        if entering_variable_index == exiting_variable_index:
            break

        pivot_column = tableau[:, entering_variable_index]

        b_vector = tableau[:, -1]
        b_divided_by_pivot_column = b_vector / pivot_column
        b_divided_by_pivot_column = np.delete(b_divided_by_pivot_column, np.where(b_divided_by_pivot_column <= 0))

        if len(b_divided_by_pivot_column) == 0:
            break

        exiting_variable_coefficient = np.amin(b_divided_by_pivot_column)
        exiting_variable_index = np.where(b_divided_by_pivot_column == exiting_variable_coefficient)[0][0] + 1

        tableau[exiting_variable_index] = tableau[exiting_variable_index] / tableau[exiting_variable_index][entering_variable_index]

        for row_index in range(len(tableau)):
            if row_index != exiting_variable_index:
                pivot_coefficient = tableau[row_index][entering_variable_index]
                row_to_add = -pivot_coefficient * tableau[exiting_variable_index]
                tableau[row_index] = tableau[row_index] + row_to_add

        tableau = np.around(tableau, 2)

    return tableau[:, -1]
