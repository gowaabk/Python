# Задание №3
# 📌 Создайте класс-генератор.
# 📌 Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# 📌 Если переданы два параметра, считаем step=1.
# 📌 Если передан один параметр, также считаем start=1.

class Generator():

    def __init__(self, *args):
        match len(args):
            case 1:
                self.start = 1
                self.stop = args[0]
                self.step = 1
            case 2:
                self.start = args[0]
                self.stop = args[1]
                self.step = 1
            case 3:
                self.start, self.stop, self.step = args

    def __iter__(self):
        return self

    def __next__(self):

        while self.start < self.stop:

            result = 1
            # for i in range(self.start, self.stop, self.step):
            for j in range(2, self.start + 1):
                result *= j
            self.start += self.step
            return result
        raise StopIteration


if __name__ == "__main__":

    fg = Generator(3, 5, 1)
    for i in fg:
        print(i)
