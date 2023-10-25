import numpy as np

def simplex(A, b, c, maximize=True):
    if maximize:
        c = -c

    m, n = A.shape
    tableau = np.zeros((m + 1, n + 1))

    tableau[:-1, :-1] = A
    tableau[:-1, -1] = b
    tableau[-1, :-1] = c

    while any(tableau[-1, :-1] < 0):
        col = np.where(tableau[-1, :-1] < 0)[0][0]
        epsilon = 1e-10
        ratios = tableau[:-1, -1] / np.where(tableau[:-1, col]==0, epsilon, tableau[:-1, col])
        row = np.argmin(ratios)
        pivot = tableau[row, col]

        if all(tableau[:-1, col] <= 0):
            print("Problema inviável. Variáveis artificiais ainda na base.")
            return None

        tableau[row, :] /= pivot

        for i in range(m + 1):
            if i != row:
                tableau[i, :] -= tableau[i, col] * tableau[row, :]

    result = tableau[-1, -1]
    variables = tableau[-1, :-n-1]
    return result, variables



def read_input(file_name):
    with open(file_name, 'r') as file:
        data = file.read().split('\n')
        m, n, maximize = map(int, data[0].split())
        c = np.array(list(map(float, data[1].split())))
        A = []
        b = []

        for i in range(2, 2 + m):
            line = data[i].split()
            inequality_index = line.index('<=') if '<=' in line else line.index('==') if '==' in line else line.index(
                '>=')
            coefficients = list(map(float, line[:inequality_index]))  # convert only numerical coefficients
            sign = line[inequality_index]  # get the inequality sign

            if sign == '<=':
                coefficients.extend([0] * i + [1] + [0] * (m - i))
            elif sign == '==':
                coefficients.extend([0] * i + [0] + [0] * (m - i))
            elif sign == '>=':
                coefficients.extend([0] * i + [-1] + [0] * (m - i))
            line = data[i].split()
            inequality_index = line.index('<=') if '<=' in line else line.index('==') if '==' in line else line.index(
                '>=')
            coefficients = list(map(float, line[:inequality_index]))  # convert only numerical coefficients
            sign = line[inequality_index]  # get the inequality sign
            b.append(float(line[inequality_index + 1]))  # get the independent term

            A.append(coefficients)

        A = np.array(A)
        b = np.array(b)
        return A, b, c, maximize

def main():
   
    while True:
        print("\nMenu Principal:")
        print("1) Executar o Simplex, mostrando resultados intermediários")
        print("2) Executar o Simplex, mostrando apenas o resultado final")
        print("3) Sair do programa")

        choice = input("Escolha uma opção (1/2/3): ")

        if choice == '1':
            file_name = input("Digite o nome do arquivo de entrada: ")
            A, b, c, maximize = read_input(file_name)
            print("Executando o Simplex, mostrando resultados intermediários:")
            z, x = simplex(A, b, c, maximize)
            if maximize:
                z = -z
            print(f"Resultado: {z}")
            print(f"Valores das variáveis: {x}")
        elif choice == '2':
            file_name = input("Digite o nome do arquivo de entrada: ")
            A, b, c, maximize = read_input(file_name)
            z, x = simplex(A, b, c, maximize)
            if maximize:
                z = -z
            print("Executando o Simplex, mostrando apenas o resultado final:")
            print(f"Resultado: {z}")
            print(f"Valores das variáveis: {x}")
        elif choice == '3':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Escolha 1, 2 ou 3.")

if __name__ == "__main__":
    main()
