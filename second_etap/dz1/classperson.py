# a) поля fullName, age, place(address)
# б) метод talk(), в которых просто вывести на консоль сообщение -"Такой-то  Person говорит". Метод
#
# move()  будет менять его адрес
# в) Добавьте  конструктор  с тремя параметрами fullName, address, age = 18
# г) Настроить  метод __str__  (Сделать отображение всех полей объекта)

class Person:
    def __init__(self, fullName, address, age=18):
        self.fullName = fullName
        self.address = address
        self.age = age


    def talk(self, name):
        return f'{name} speaks'

    def move(self, new_address):
        self.address = new_address

    def __str__(self):
        return f'persons name is {self.fullName} and his/her address is {self.address}, his/her age is {self.age}'

Aichurek = Person('Aichurek', 'LifeTowers', 33)
print(Aichurek)

