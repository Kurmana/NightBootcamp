# Чтение из файла.
# Создайте файл с текстом The Zen of Python.
# Напишите функцию, которая считайте его и возвратит список из слов, которые начинаются на букву “c” или “C”.
# Подсказка: используйте метод строчных значений, который проверяет, начинается ли слово на переданную букву.


# with open('text.py', 'r') as my_file:
#     data = my_file.read()

# r = data.split(' ')
# c_words = []
# for i in r:
#     if 'c' in i:
#         c_words.append(i)
#         print(c_words)

#Второй вариант
#with open('text.py', 'r') as my_file:
#     read = file.readlines()
#     read_str = ''.join(read).lower()
#     splited = read_str.split()
#     for i in splited:
#         if letter in i:
#             print(i)

