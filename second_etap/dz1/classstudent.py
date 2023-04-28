# Создайте класс Student, конструктор которого имеет параметры name, lastname,
# department, year_of_entrance. Добавьте метод get_student_info, который
# возвращает имя, фамилию, год поступления и факультет в
# отформатированном виде: “Вася Иванов поступил в 2017 г. на факультет:

class Student:
    def __init__(self, name, last_name, department, year_of_entrance):
        self.name = name
        self.last_name = last_name
        self.department = department
        self.year_of_entrance = year_of_entrance

    def get_student_info(self):
        return f'{self.name} {self.last_name} entered the university in {self.year_of_entrance} majoring in {self.department}'

Vasya = Student('Vasya', 'Ivanov', 'programming', '2008')
print(Vasya.get_student_info())