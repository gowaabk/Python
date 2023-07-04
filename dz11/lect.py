# class User:
#     def __init__(self, name: str) -> None:
#         self.name = name
#         print(self.name)

#     def __str__(self):
#         return f"{self.name=}"

#     def __del__(self):
#         return f'Удалил {self.name}'


# u1 = User("sdf")
# u2 = User("sdf_2")

# print(u1, u2)
# del u1

# print(u1, u2)

class Rectangle:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b

    def __str__(self) -> str:
        return f"квадрат {self.a} {self.b} {self.c}"

    def __add__(self, other):
        self.c = self.a - self.b
        return self.c


u1 = Rectangle(5, 5)
print(u1+u1)
