# Идентификационный номер, Фамилия, Имя, Отчество, Адрес, Номер кредитной карточки,
# Дебет, Кредит, Время междугородных и городских переговоров;
# Конструктор;
# Методы: установка значений атрибутов, получение значений атрибутов, вывод информации.
# Создать массив объектов данного класса. Вывести сведения относительно абонентов, у
# которых время городских переговоров превышает заданное.  Сведения относительно абонентов,
# которые пользовались междугородной связью. Список абонентов в алфавитном порядке.

class Abonent:
    def __init__(self, id, last_name, name, fathers_name, address, credit_card_number, debit, credit, speaking_time):
        self.id = id
        self.last_name = last_name
        self.name = name
        self.fathers_name = fathers_name
        self.address = address
        self.credit_card_number = credit_card_number
        self.debit = debit
        self.credit = credit
        self.speaking_time = speaking_time


