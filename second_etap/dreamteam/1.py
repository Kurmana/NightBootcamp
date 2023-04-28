## 1
# AK-47:
# У солдата Райана есть АК-47
# Солдаты могут стрелять («тиги-тигитиш»).
# Пистолеты могут стрелять пулями.
# Пистолеты могут начинать патроны - увеличивайте количество патронов (перезаряжает)
# Создайте класс Act_of_Shooting, который унаследует от класса Soldier класс Guns.
# Где солдат будет стрелять из пушки и перезаряжаться, и стрелять еще раз.
import random
# class Soldier:
#     def __init__(self, name):
#         self.name = name
#
#
# class Guns (Soldier):
#     def __init__(self, name, gun, boolets):
#         super().__init__(name)
#         self.gun = gun
#         self.boolets = boolets
#         self.shoot = boolets
#
#     def shooting(self):
#         if self.boolets > 0:
#             print('pam pam')
#             self.shoot -= 1
#
#         else:
#             return f'please reload'
#
#
#     def recharge(self):
#         self.boolets = self.shoot
#         return f'the gun is reloaded'
#
# class Act_of_Shooting (Guns, Soldier):
#     def __init__(self, name, gun, boolets):
#         super().__init__(name, gun, boolets)
#
#     def shooting_non_stop(self):
#         self.shooting()
#         if self.boolets == 0:
#             self.recharge()
#             self.shooting()
#
#
#
#
# n = Act_of_Shooting(name='Rayan', gun='АК-47', boolets=1)
# print(n.shooting_non_stop())
# print(n.shooting_non_stop())



# # 2
# Furniture:
# Тип дома, общая площадь и перечень наименований мебели В новом доме совсем нет мебели.
# Мебель имеет название и площадь, из которых Спальня: 4 квадратных метра Гардероб: 2 квадратных метра Стол: 1,5 квадратных метра.
# Добавьте в дом три вышеупомянутых предмета мебели.
# При печати дома требуются следующие данные: тип дома, общая площадь, оставшаяся площадь, список названий мебели.


# class House:
#     def __init__(self, house_type, square_meters):
#         self.house_type = house_type
#         self.square_meters = square_meters
#
#
# class Furniture(House):
#     def __init__(self, house_type, square_meters):
#         super().__init__(house_type, square_meters)
#         self.bedroom = 4
#         self.wardrobe = 2
#         self.table = 1.5
#         self.furniture_title = 'bedroom, wardordrobe and table'
#
#     def add_furniture(self):
#         return f'we added {self.bedroom}, {self.wardrobe} and {self.table}'
#
#     def data_home(self):
#         return f'our {self.house_type} has {self.square_meters} total square meters and the remaining sqaure is {self.square_meters - self.bedroom - self.wardrobe - self.table}. Here is the list of the furniture we have purchased so far: {self.furniture_title}'
#
# H1 = Furniture('villa', 100)
# print(H1.data_home())


# # 3
# Students room:
# Реализуйте студенческую комнату с помощью ООП:

# Copy:
# Steve = Student("Steven Schultz", 23, "English")
# Johnny = Student("Jonathan Rosenberg", 24, "Biology")
# Penny = Student("Penelope Meramveliotakis", 21, "Physics")
# print(Steve)
# <name: Steven Schultz, age: 23, major: English>
# print(Johnny)
# <name: Jonathan Rosenberg, age: 24, major: Biology>



# class Student:
#     def __init__(self, name, age, major):
#         self.name = name
#         self.age = age
#         self.major = major
#
#     def __str__(self):
#         return f'<name: {self.name}, age: {self.age}, major: {self.major}>'
#
#
# Steve = Student("Steven Schultz", 23, "English")
# Johnny = Student("Jonathan Rosenberg", 24, "Biology")
# Penny = Student("Penelope Meramveliotakis", 21, "Physics")
# print(Steve)
# print(Johnny)


# # 4
# Dollar
# Создайте функцию dollarize (), которая принимает Float и возвращает долларовый формат:

# Copy
# dollarize(123456.78901) -> "$123,456.80"
# dollarize(-123456.7801) -> "-$123,456.78"
# dollarize(1000000) -> "$1,000,000"

# Преобразуйте эту функцию в полезный класс MoneyFmt. MoneyFmt содержит одно значение данных (количество) и 4 метода.
# Copy
#     "init" //конструктор инициализирует значение данных done
#     "update" //метод заменяет значение данных новым done
#     "repr" //методы возвращают значение с плавающей запятой done
#     "str" //метод, реализующий логику метода dollarize () done

# Copy
# //Результат будет выглядеть так:
# import moneyfmt
# cash = moneyfmt.MoneyFmt(12345678.021)
# print(cash) -- returns "$12,345,678.02"
# cash.update(100000.4567)
# print(cash) -- returns "$100,000.46"
# cash.update(-0.3)
# print(cash) -- returns "-$0.30"
# repr(cash) -- returns -0.3

# class Moneyfarm:
#     def __init__(self, number: float):
#         self.number = number
#
#     def __float__(self):
#         return f'$ {self.number}'
#
#
#     def update(self, new_number):
#         self.number = new_number
#         return new_number
#
#
#     def __repr__(self):
#         return f'$ {float(self.number)}'
# ## строгий возвращает состояние для объектов, а str  возвр строку для всех
#
#
#     def __str__(self):
#         return f'$ {self.number}'
#
# # dollarize =  Moneyfarm(1000000)
# dollarize = Moneyfarm(123456.78901)
# print(dollarize.__repr__())
# print(dollarize.update(231))


# 5
# Deck of Cards:
# Создайте класс колоды карт. Внутри колода карт должна использовать другой класс - класс карт. Ваши требования:
# Класс Deck должен иметь метод раздачи для раздачи одной карты из колоды.
# После раздачи карты она удаляется из колоды.
# Должен быть метод «смешивания», который проверяет, что в колоде есть все 52 карты, а затем меняет их случайным образом.
# Класс должен иметь масть (червы, бубны, трефы, пики) и ценность карты (A, 2,3,4,5,6,7,8,9,10, J, Q, K)
# ПРИМЕЧАНИЕ: используйте случайное перемешивание

# Copy
#
# from random import shuffle
# class Cards:
#
#     def __init__(self, suit, rank):
#         self.suit = suit
#         self.rank = rank
#
#
#     def __str__(self):
#         return f'{self.rank} {self.suit} '
#
#
# class Deck:
#     def __init__(self, cards):
#         self.cards = cards
#         self.card_num = 52
#
#     def deck_info(self):
#         for card in self.cards:
#             print(card)
#
#     def mix_card(self):
#         random.shuffle(self.cards)
#
#     def one_card(self):
#         if not self.cards:
#             return 'no card'
#         return random.choice(self.cards)
#
#     def pick_card(self):
#         return [self.one_card() for _ in range(self.card_num)]
#
#
# rank = ['A', '2','3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
# suit = ['червы', 'бубны', 'трефы', 'пики']
# cards = [Cards(s, r) for s in suit for r in rank]
#
# deck = Deck(cards)
# deck.mix_card()
# print()
# print('перемешанная колода')
# deck.deck_info()
# print(deck.pick_card())
# print()
