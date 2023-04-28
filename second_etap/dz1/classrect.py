# Построить
# класс для описания плоской геометрической фигуры: Rectangle (Прямоугольник.).
# Класс
# должен содержать:
# Данные:
# длина и ширина прямоугольника
# Методы для операций с данными:

class Ractangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def square(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

a = Ractangle(4, 5)
print(a.square())
print(a.perimeter())