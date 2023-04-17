


# Problem_2
#Спросите у пользователя 5 чисел добавьте их в SET и скажите какое самое маленькое число он ввел.

# n_0 = int(input('please enter 5 numbers - '))
# x = set(str(n_0))
# print(min(x))

# Problem_3
# просить у пользователя Python ФУНКЦИЮ и если такая есть исполнить и
# вернуть пользователю результат иначе сказать что в Python такой функции нет!
# fun = input('please enter a function - ')
# list = list(input('your list - '))
# for i in fun:
#     if i == 'all()' or i == 'min()' or i == 'max()' or i == slice():
#         print(list(fun))
#     else:
#         print('this function doesnt exist')

# Problem_4
# Спросите у пользователя сумму займа(не меньше 50 000) и посчитайте сколько нужно будет вернуть если % = 3.47, результат округлите до 2 чисел после точки.
# Формула подсчёта переплаты: Сумма * (% / 100)

# summ = int(input('please enter the amount, not less than 50 000 - '))
# total = summ * (33.47 / 100)
# print(round(total, 2))

# Problem_1
#typeerror
# a = ('b', 'n', 23, 'large', 12.4)
# n = {234, 'kino'}
# summ = a + n
# print(summ)
#IndexError,
# a = ('b', 'n', 23, 'large', 12.4)
# print(a[6])
# NameError
# a = ('b', 'n', 23, 'large', 12.4)
# print(b)

# Problem_2
#Возьмите код #1 и создайте для него try... except... Создайте несколько except выражений для разных типов ошибок.
# at = 10
# inn = 15
# wo = 20
#
# for e in range(-at, at):
#     print(wo / e)
# try:
#     if at > '5':
#         print("at > 5")
#
# except:
#     print('error, enter again')


# Problem_3 сделайте так чтобы работал. Если не знаете как исправить ошибку создайте для неё except выражение.
# lst = []
# for i in renge(10):
# lst.apend(i)
#
# a = list(revesed(lst))
# sls_obj = slice('0','8')
# print(а[sls_obj])

# Problem_4 исправьте все ошибки, сделайте так чтобы код работал. Если не знаете как исправить ошибку создайте для неё except выражение.

# a = (0)
# b = (1,)
# numbers = []
# while b > a:
# numbers += b
# b += 1

# Problem_1 словать ключи должны быть только строковыми объектами, но может встретиться Int, как в качестве ключа,
# но ваша проверка только проверяет на строку и поэтому у вас выходит баг, ваша задача обработать исключением ошибку TypeError
# dict_ = {'name': 'john', 'lastname': 'Snow', 12: 'age'}
# for x in dict_.keys():
# x + 'abc'