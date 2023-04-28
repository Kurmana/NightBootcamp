# а) Создайте класс Phone, который содержит атрибуты number, model и
# weight.
# б) Создайте три экземпляра этого класса.
# в) Выведите на консоль значения их атрибутов.
# г) Добавить конструктор в класс Phone, который принимает на вход три параметра для
# инициализации переменных класса - number, model и weight.
# д) Создать метод sendMessage. Данный метод принимает на вход номера телефонов, которым
# будет отправлено сообщение. Метод выводит на консоль номера этих телефонов.


class Phone:
    def __init__(self, number, model, weight):
        self.number = number
        self.model = model
        self.weight = weight

    def send_message(self):
        return f'message will be sent to the following number {self.number}'

Iphone = Phone(211768634, 13, 2)
Sumsung = Phone(21314176876, 'S4', 1.4)
Nokia = Phone(46785578, 'i230', 1.9)

# print(Iphone.__str__())
# print(Sumsung.__str__())
# print(Nokia.__str__())

print(Sumsung.send_message())