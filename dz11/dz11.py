# Решить задачи, которые не успели решить на семинаре.
# Добавьте ко всем задачам с семинара строки документации и методы вывода
# информации на печать.
# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц


class Matrix:
    """Класс матрица с инициализацией списка списков,с переопределенными
     методами сложения и вывода на печать"""

    def __init__(self, matrix_list: list[list[int]]):
        """Инициализация экземпляра матрицы"""
        self.matrix_list = matrix_list

    def __str__(self):
        """Вывод матрицы на печать."""
        result = ""
        for row in self.matrix_list:
            for elem in row:
                result += ''.join(f'{elem}\t')
            result += ''.join('\n')
        return result

    def __eq__(self, other):
        """Переопределённый метод для сравнения матриц.
        Сравнивается по длине и каждому элементу."""
        if self.matrix_list != other.matrix_list:
            return False
        else:
            return True

    def __add__(self, other):
        """Переопределение метода сложения матриц.
        Можно складывать матрицы одинаковых размеров"""
        result = []
        row = []
        for i in range(len(self.matrix_list)):
            for j in range(len(self.matrix_list[0])):
                row.append(self.matrix_list[i][j] + other.matrix_list[i][j])
            result.append(row)
            row = []
        return Matrix(result)


if __name__ == "__main__":
    matrix_1 = Matrix([[3, 2, 3], [4, 5, 6], [7, 8, 9]])
    matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matrix_sum = matrix_1 + matrix_2
    print(matrix_1)
    print(matrix_2)
    print(matrix_sum)
    print(matrix_1 == matrix_2)