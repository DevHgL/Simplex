import numpy as np

def read_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    m, n, maximize = map(int, lines[0].split())
    c = np.array(list(map(float, lines[1].split())))
    A = []
    b = []

    for line in lines[2:]:
        parts = line.split()
        coefficients = list(map(float, parts[:-1]))
        if parts[-1] == '<=':
            coefficients += [0.0] * (m - len(coefficients)) + [1.0]
        elif parts[-1] == '==':
            coefficients += [0.0] * (m - len(coefficients)) + [-1.0]
        else:
            coefficients += [0.0] * (m - len(coefficients)) + [-1.0]
            coefficients.append(1.0)
        A.append(coefficients)
        b.append(float(parts[-2]) * -1 if parts[-1] == '>=' else float(parts[-2]))

    return c, np.array(A), np.array(b), maximize

def simplex(c, A, b, maximize):
    m, n = A.shape
    c = np.concatenate([c, np.zeros(m)])
    A = np.column_stack([A, np.eye(m)])
    x = np.zeros(n + m)
    basis = np.arange(n, n + m)
    obj_value = np.inf

    while True:
        reduced_costs = c - np.dot(c[basis], np.linalg.inv(A[:, basis]))
        if maximize:
            entering = np.argmax(reduced_costs)
        else:
            entering = np.argmin(reduced_costs)

        if reduced_costs[entering] >= 0:
            break

        ratios = b / A[:, entering]
        ratios[ratios < 0] = np.inf
        leaving = np.argmin(ratios)

        x[entering], x[basis[leaving]] = ratios[leaving], 0
        basis[leaving] = entering

        pivot = A[leaving, entering]
        A[leaving, :] /= pivot
        b[leaving] /= pivot

        for i in range(m):
            if i != leaving:
                factor = A[i, entering]
                A[i, :] -= factor * A[leaving, :]
                b[i] -= factor * b[leaving]

        obj_value = np.dot(c[basis], np.linalg.inv(A[:, basis]))

    return obj_value, x[:n]

if __name__ == "__main__":
    c, A, b, maximize = read_input("problema1.txt")
    obj_value, solution = simplex(c, A, b, maximize)
    print("Objective Value:", obj_value)
    print("Solution:", solution)
