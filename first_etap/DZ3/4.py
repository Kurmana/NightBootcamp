dict_one = {'a':1, 'b':2, 'c':3}
dict_two = {'d':4, 'e':5, 'f':6}
dict_three = {'g':7, 'h':8, 'i':9}
dict_four = {}
# С помощью цикла for необходимо собрать три первых словаря в словарь dict_four
# Подсказка: Для удобства итерации, первые три словаря можно записать в кортеж (dict_one, dict_two, dict_three

for key, value in dict_one.items():
    dict_four[key] = value
for key, value in dict_two.items():
    dict_four[key] = value
for key, value in dict_three.items():
    dict_four[key] = value

    print(dict_four)