import numpy as np

def create_tableau(objective_coefficients, constraint_coefficients, independent_terms, optimization_type, constraint_operations):
    num_constraints = len(constraint_coefficients)
    num_variables = len(objective_coefficients)

    tableau = np.zeros((num_constraints + 1, num_variables + num_constraints + 1))

    # Set up the objective function in the first row of the tableau
    tableau[0, :num_variables] = objective_coefficients

    for i in range(num_constraints):
        if independent_terms[i] < 0:
            tableau[0] = -tableau[0]
            independent_terms = -independent_terms
            if constraint_operations[i] == "<=":
                constraint_operations[i] = ">="
            elif constraint_operations[i] == ">=":
                constraint_operations[i] = "<="

    # Set up constraints and independent terms
    for i in range(num_constraints):
        tableau[i + 1, :num_variables] = constraint_coefficients[i]
        tableau[i + 1, num_variables + i] = 1 if constraint_operations[i] == '<=' or constraint_operations[i] == '==' else -1  # Adding slack or surplus variables
        tableau[i + 1, -1] = independent_terms[i]

    return tableau
