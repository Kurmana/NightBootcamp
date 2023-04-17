# Должен знать либо python, либо java, либо javascript. Возраст от 18 до 65. Опыт
# от 3х лет. Зарплата до 60000. Вывести результат, подходит кандидат или нет.

language = input('язык програмирования -')
age = int(input('возраст - '))
experience = int(input('опыт работы -'))
salary = int(input('зарплата - '))
if language == 'python' or language == 'java' or language == 'javascript':
    if 18 < age < 65 and experience >= 3 and salary <= 60000:
        print('вы приняты')
else:
    print('мы не можем далее рассматривать вашу кандидатуру')