# # Problem_1
# def multiply(a, b, c):
#     print('Объем бассейна', a*b*c)
#
#
# multiply(3, 2, 4)
import random


# swimming_pool = lambda a, b, c: a * b * c
#
# print('Объем бассейна', swimming_pool(2, 4, 6))

# Problem_2
# d = lambda x: 365 - x
#
# print('до нового года осталось', d(33))

# Problem_3
# def rec(x):
#     if x%2 != 0:
#         print(x)
#         rec(x+2)
#         print(x)
#     else:
#         print('even number')
#
# rec(333)

# Problem_4 НЕ решила
# Напишите функцию которая принимает SET и рекурсивно удаляет оттуда по одному элементу при запуске.

# def rec('SET'):
#     for value in 'SET':
#         a = []
#         a.append(value)
#         s.discard(a[0])
#         return rec(s)
#
# print(rec('set'))


# Problem_ 4
# Напишите функцию которая генерирует 100 рандомных чисел в диапазоне от 10 до 50 и возвращает их в листе.
# Напишите ДЕКОРАТОР для этой функции которая удалит все дубликаты в первой функции и вернёт всё так же лист.

# from random import randint
#
#
# # def delete_dubl(func):
# #     def wrapper():
# #         data = func()
# #         return list(set(data))
# #     return wrapper
# #
# #
# # @delete_dubl
# def random_list():
#     return [randint(10, 50) for i in range(100)]


# print(random_list())



