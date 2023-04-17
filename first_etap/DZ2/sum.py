# Ввести число любой длины.
# Вывести на экран сумму его цифр.

number = int(input("Введите целое: "))
summ = 0
for i in str(number):
    summ = summ + int(i)
    print(summ)

