# #открылся file people.txt и там будет имя айчурек
# my_file = open('people.txt', 'w')
# name = input('enter name - ')
# my_file.write(name)
# my_file.close()
#

##выдает то что в файле people.txt. можно в ручную поменять в том файле и тут выведет
# my_file = open('people.txt', 'r')
# data = my_file.read()
# print(data)
# my_file.close()


# my_file = open('people.txt', 'r')
# with open('people.txt', 'r') as my_file:
#     print('opened')
# print('closed')


# Problem_2 , ignore Problem_1
# with open('users.txt', 'w') as my_file:
#     login= input()
#     password = input()
#     my_file.write(login + ' ' + password)

#Problem_3
#Создайте программу, которая считает из файла текст, и если в тексте содержится буква “w”, то
# выведет на экран “Да, в тексте есть w”, иначе - “Нет, в тексте нет w”. Подсказка: используйте ключевое слово in.

# with open('text3.txt', 'w') as my_file:
#      sent= input('enter a text')
#      my_file.write(sent)
#      my_file.close()
#
# with open('text3.txt', 'r') as my_file:
#     if 'w' in sent:
#         print('hai')
#     else:
#         print('iee')

#Problem_3
# Создайте текстовый файл python.txt и запишите в него текст #1:
# Затем, считайте его. Пробежитесь по всем его словам, и если слово содержит
# букву “t” или “T”, то запишите его в список t_words = [ ]. После окончания списка,
# выведите на экран все полученные слова. Подсказка: используйте for.

with open('python.txt', 'w') as my_file:
    enter = '''
    Python is a widely used high-level programming language
    for general-purpose programming, created by Guido van Rossum
    and first released in 1991. An interpreted language, Python has
    a design philosophy that emphasizes code readability (notably using
    whitespace indentation to delimit code blocks rather than curly
    brackets or kewords), and a syntax that allows programmers to
    express concepts in fewer lines of code than might be used in languages such as C++ or Java.
    '''
    my_file.write(enter)

with open('python.txt', 'r') as my_file:
    data = my_file.read()

r = data.split(' ')
t_words = []
for i in r:
    if 't' in i:
        t_words.append(i)
print(t_words)

# Prblem_1

#Создайте database.txt файл с несколькими логинами и паролями. Затем попросите пользователя войти или зарегистрироваться.
# Спросите его логин и пароль. Если такой логин уже есть скажите ему что логин уже существует и предложите зарегистрироваться спросив пароль.
# Если такого логина неоказалось среди уже существющих
# продолжайте регистрацию. Спросите у него Пароль 2 раза и сохраните в в файл datebase.txt только если пароли совпадают.

# a = 'asd 122 fdgdfg 123 lala 344'
# with open('database.txt', 'w') as f:
#     f.write(a)
#
# with open('database.txt', 'r') as f:
#     data = f.read()
#
# users = data.split(' ')
# print(users)
#
# login = input()
# password = input()
#
# for i in users:
#     if login == i.split(' ')[0]:
#         print('user exists, please enter password')
#         password1 = input()
#         while True:
#             if password1 == password and password1 == i.split(' ')[1]:
#                 print('you entered')
#                 break
#             else:
#                 print('try again')
#         break
# else:
#
#     password2 = input()
#     if password == password2:
#         with open('database.txt', 'a') as f:
#             f.write(' ' + login + ' ' + password)
#             print('successful registration')

