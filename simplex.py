import numpy as np
import sys
from resolve import simplex_algorithm 
from cria_tableau import create_tableau

def convert_array_to_float(array):
    return list(map(lambda val: float(val), array))

def convert_array_to_int(array):
    return list(map(lambda val: int(val), array))

if __name__ == '__main':
    if len(sys.argv) >= 2:
        file_path = sys.argv[1]
    else:
        file_path = str(input("Digite o caminho do arquivo: "))

    with open(file_path, "r") as file:
        file_content = file.read()
    file_lines = file_content.split('\n')

    num_constraints, num_variables, optimization_type = convert_array_to_int(file_lines[0].split(' '))
    objective_function_coefficients = convert_array_to_float(file_lines[1].split(' '))

    objective_function_coefficients = np.array(objective_function_coefficients)

    constraint_coefficients = []
    operations = []
    independent_terms = []

    for i in range(num_constraints):
        *coefficients, operation, independent_term = file_lines[2 + i].split(' ')

        constraint_coefficients.append(convert_array_to_float(coefficients))
        operations.append(operation)
        independent_terms.append(float(independent_term))

    constraint_coefficients = np.array(constraint_coefficients)
    operations = np.array(operations)
    independent_terms = np.array(independent_terms)

    tableau = create_tableau(objective_function_coefficients, constraint_coefficients, independent_terms, optimization_type, operations)  # Chamei a função corretamente
    solution = simplex_algorithm(np.copy(tableau), optimization_type)  # Chamei a função corretamente

    print(solution)
    print(tableau)
