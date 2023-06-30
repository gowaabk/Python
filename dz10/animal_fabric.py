# Задание №5
# 📌 Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# 📌 У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# 📌 Для каждого класса создайте метод, выводящий
#  информацию специфичную для данного класса.

# Задание №6
# 📌 Доработайте задачу 5.
# 📌 Вынесите общие свойства и методы классов в класс
# Животное.
# 📌 Остальные классы наследуйте от него.
# 📌 Убедитесь, что в созданные ранее классы внесены правки.

class Animals():

    def __init__(self, name: str, weight: int, age: int):
        self.name = name
        self.weight = weight
        self.age = age

    def move(self):
        pass

    def say(self):
        pass

    def __str__(self):
        return f'{self.name} {self.weight} {self.age}'


class Birds(Animals):
    def __init__(self, name: str, weight: int, age: int, bird_type: str, sound: str):
        super().__init__(name, weight, age)
        self.bird_type = bird_type
        self._sound = sound

    def move(self):
        return "FLY"

    def say(self):
        return self._sound

    def __str__(self):
        return f'{super().__str__()} {self.bird_type}'


class Dogs(Animals):
    def __init__(self, name: str, weight: int, age: int, dog_type: str):
        super().__init__(name, weight, age)
        self.dog_type = dog_type

    def move(self):
        return "RUN"

    def say(self):
        return "GAV"

    def __str__(self):
        return f'{super().__str__()} {self.dog_type} '


class Fish(Animals):
    def __init__(self, name: str, weight: int, age: int, fish_type: str):
        super().__init__(name, weight, age)
        self.fish_type = fish_type

    def move(self):
        return "SWIM"

    def say(self):
        return ""

    def __str__(self):
        return f'{super().__str__()} {self.fish_type}'

# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.


class Fabric:

    def create_animal(self, animal_type: str, *args, **kwargs):
        new_animal = self.get_maker(animal_type)
        return new_animal(*args, **kwargs)

    def get_maker(self, animal_type: str):
        types = {"dogs": Dogs, "birds": Birds, "fish": Fish}
        return types[animal_type.lower()]


if __name__ == '__main__':
    # dog1 = Dogs("Jess", 14, 4, "Dvoryanka")
    # bird1 = Birds("Гоша", 5, 2, "ara", "krya")
    # fish1 = Fish("Arpa", 1, 4, "karp")

    # print(dog1)
    # print(bird1)
    # print(fish1)

    fabric = Fabric()
    fabric_animal = fabric.create_animal("Dogs", "Jess", 14, 4, "Dvoryanka")
    print(fabric_animal)
