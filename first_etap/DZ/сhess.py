a = int(input('введите число от 1 до 8 первая клетка- '))
b = int(input('введите число от 1 до 8 первая клетка - '))
c = int(input('введите число от 1 до 8 вторая клетка - '))
d = int(input('введите число от 1 до 8 вторая клетка - '))
x = a - c
y = b - d
if -1 <= x <= 1 and -1 <= y <= 1:
    print('yes')
else:
    print('no')