# Напишите функцию для транспонирования матрицы

# Читаемый вывод матриц
def pretty_print(new_list: list) -> list:
    for i in new_list:
        print(i)

    return print()

# Транспонирование матрицы


def matrix_transpon(matrix: list) -> list:
    for i in matrix:
        if len(i) != len(matrix[0]):
            print("Матрицу нельзя транспонировать")
            break
    new_matrix = []
    for i in range(len(matrix[0])):
        new_matrix.append([0]*len(matrix))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix

def matrix_transpon_zip(matrix: list) -> list:
    return list(zip(*matrix))



matrix = ([1, 2, 3],
          [4, 5, 6])

pretty_print(matrix)
# 1-й вариант транспонирования
pretty_print(matrix_transpon(matrix))

# 2-ой вариант транспонирования
# pretty_print(list(zip(*matrix)))

pretty_print(matrix_transpon_zip(matrix))
