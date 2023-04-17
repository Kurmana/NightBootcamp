# Выберите действие:
# 1. Добавить новый город
# 2. Отобразить список городов
# 3. Заменить город
# 4. Удалить город
# 5. Выход

start = 1
list_cities = {'Dubai', 'Moscow', 'Amsterdam'}
new_cities = 'A'
see_list = 'B'
change_city = 'C'
delete_city = 'D'


while start <=1:
    try:
        action = input(
            'press A if want to add a new city, press B if want to see the list of cities, press C change a city, press D to delete a city, press E if want to exit - ')

        if action == 'A':
            M = input('enter a city')
            if M in list_cities:
                print('it already exists', list_cities)
            else:
                list_cities.add(M)
                print('the city has been added', list_cities)

        if action == 'B':
            print(list_cities)

        if action == 'C':
            print('current_city', list_cities)
            S = input('enter the city you want to change - ')
            N = input('new city - ')
            if N not in list_cities:
                list_cities.add(N)
                list_cities.remove(S)
                print('well noted, added', list_cities)
            else:
                print('it already exists')

        if action == 'D':
            print('current city -', list_cities)
            M = input('enter a city you would like to delete - ')
            if M in list_cities:
                list_cities.remove(M)
                print('the city has been deleted', list_cities)
            else:
                print('it is not in the list')

        if action == 'E':
            print('bye')
            break
    except ValueError:
        print('incorrect name')



