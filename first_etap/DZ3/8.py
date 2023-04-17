# Написать функцию season, принимающую
# 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года,
# которому этот месяц принадлежит (зима, весна, лето или осень).

def season(x):
    if x <= 2 or x == 12:
        return 'winter'
    elif 3 <= x <= 5:
        return 'spring'
    elif 6 <= x <=8:
        return 'summer'
    elif 9 <= x <= 11:
        return 'fall'

print(season(12))
