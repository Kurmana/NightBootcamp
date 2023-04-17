#как запросить у пользователя три раза логин и пароль и вывести в качестве диктионери
# data = {}
#
# for i in range(3):
#     login = input('Введите логин - ')
#     password = input('Введите пароль - ')
#     data[login] = password
#
# print(data)
#
#IN/NOT IN - проверить есть ли какой либо объект в списке или листе

# a = [1, 2, 'das', 'i']
# m = input()
# if m not in a:
#     print(True)
# else:
#     print(False)

# k = int(input("Вместимость сковороды: "))
# m = int(input("Минуты: ")) * 2
# n = int(input('Котлеты: '))
#
# if n % k == 0:
#     print(n//k * m)
# else:
#     print(n // k * m + m)


#names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
#
# for i in range(len(names)):
#   if i % 2 ==0:
#     print(names[i])

# total = ''
# for i in range(10):
#   total += str(i) + ', '
#
# for i in range(10, 0, -1):
#   total += str(i) + ', '
#
#
# print(total)



#проверить, есть ли данный язык в списке

# lang1 = 'php'
# languages = ['go', 'java', 'php', 'Rust', 'python', 'javascript', 'ruby']
#
# for i in languages:
#   print(i)
#   if i == lang1:
#     print('Язык в списке')
#     break

# УЗНАТЬ подходит ли кандидат
# lang = input("Ваш язык программирования: ")
# age = int(input("Ваш возраст - "))
# exp = int(input("Ваш опыт: "))
# salary = int(input("Желаемая зарплата: "))
# if lang == 'python' or lang == 'java' or lang == 'javascript':
#   if 18 < age < 65 and exp >= 3 and salary <= 60000:
#     print('Вы приняты')

#текст - первая часть с большой буквы, а вторая часть с маленькой буквы
# a = input()
# first = a[0:len(a)//2]
# second = a[len(a)//2:len(a)]
# print(first.upper()+second.lower())

# a = '''
#         *
#        ***
#        ****
#       ******
#      ********
#     **********
#      ********
#       ******
#        ****
#         ***
#          *
#          '''
# print(a)

# a = '23554765'
# b = a[3]
# print(b)

# a = input()
# b = a[len(a), - 1]
# print(b)

# a = 'getready'
# b = a.split('t')
# print(b)

# weather = 'sunny'
# i = 10
# while weather == 'sunny':
#     i += 1
#     print('good')
#     break

# password = input('enter password - ')
# password1 = input(' enter again- ')
# while password != password1:
#     print('doesnt match')
#     print('try again')
#     password = input('enter password - ')
#     password1 = input(' enter again- ')
# else:
#     print('accepted')

# for i in range(10):
#     print(i+i)

# lang1 = 'rust'
# lang = ['go', 'java', 'python', 'php']
# for i in lang:
#     print(i)
#     if i == lang1:
#         print('in the list')
#         break

# number = 7
# for i in range(3):
#     number = number*number
#     print(number)


# total = ' '
# # for i in range(10):
# #     total += str(i) + ', '
# for i in range(10, 0, -1):
#     total += str(i) + ', '
#     print(total)


# while 1 == 1:
#     print('yes')
#     break

# i = 1
# while 1<6:
#     print(i)
#     i += 1
#     break

# i = 20
# while i >=10:
#     print(i)
#     i -= 2

# guess = input('enter ')
# password = 'gigi'
# while guess != password:
#     print('try again')
#     guess = input('enter ')
# else:
#     print('well done')


# a = [1, 2, 3] * 5
# # print(a)
# a.remove(3)
# print(a)

# for i in range(5):
#     print(i)

# for i in range(3):
#     print('aichurek')


#check problem 9 cycles
# first = 0
# second = 0
# for i in range(-100, 100):
#     if i%13 == 0:
#         first += 1
#         if i%2 == 0:
#             i = i**2
#     if i %7 == 0 and i%2 != 0:
#         second += 1
#         print('first condition')

#not clear the proeblem - check
# a = ' '
# for i in range(5, 20):
#     a += str(i) + ' '
#     if i % 7 == 0:
#         print(a)

# a = ' '
# for i in range(5, 10):
#     a += str(i) + ' '
#     if i % 7 == 0:
#         print(a)

#not clear the problem question
# names = ['mark', 'aron', 'oliver']
# new_names = []
# for i in range(len(names)):
#     if i%2 == 0:
#         new_names.append(names[i])
#         print(new_names)
#
# for i in new_names:
#     names.remove(i)
#     print(names)

# a = ['da']
# print(len(a))

# for i in range(len('qwerty')):
#     print("aichurek")


# first = [1, 2, 3, 4, 5]
# for i in first:
#     print(i**2)

# i = 1
# while i<6:
#     print(i)
#     i += 2

# str = 'yes'
# for i in str:
#     print(i)


# a = 'wegwefgwe'
# print(a[1:])
# print(a[:4])

# food = {
#     'drinks': 'coca-cola',
#     'food': 'humburger',
#     'mother': {
#         'name': 'aigul',
#         'age': '53'
#     },
#     'sister': 'aiganysh'
# }
# print(food['mother'])

# for i in food.keys():
    # print(food[i])
    # print(food.items())

# data = {
#     'name': 'Aichurek',
#     'age': '33',
#     'favourite game': ['little nightmares', 'last of us']
# }
# data['name'] = 'achu'
# data['age'] = '22'
# print(data)
# # все данные изначальные поменялись
#
# data['last_name'] = 'kurmanbekova'
# print(data)
# #добавил фамилию
#
# data['favourite game'].append('Resident Evil')
# print(data)
# # добавил в список [] с играми еще одну игру


