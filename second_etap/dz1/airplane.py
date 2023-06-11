# Создайте новый класс Airplane. Создайте следующие характеристики (полей)
# объекAта:
# ● make (марка)
# ● model
# ● year
# ● max_speed
# ● odometer
# ● is_flying
# ﻿
# и методы имитирующих поведение самолета take off (взлет), fly (летать), land
# приземление). Метод take off должен изменить is_flying на True, а land на False. По
# умолчанию поле is_flying = False. Метод fly должен принимать расстояние полета и
# изменять показания одометра (километраж). Создайте 1 объект класса и используйте
# все методы класса.

class Airplane:
    def __init__(self, marka, model, year, max_speed, odometer):
        self.marka = marka
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = odometer
        self.is_flying = False

    def take_off(self):
        self.is_flying = True
        return self.is_flying

    def fly(self):
        if self.max_speed < self.odometer//4:
            raise 'not enough fuel'
        a = self.odometer//4
        self.max_speed -= a
        print(f'waisted {a} fuel')

    def land(self):
        self.is_flying = False
        return self.is_flying



TU154 = Airplane('TU154', 'TU', 2020, 10000, 500)
print(TU154.take_off())
print(TU154.land())
print(TU154.fly())