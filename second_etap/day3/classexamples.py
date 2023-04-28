class Car:
    def __init__(self, year, marka, engine, color):
        self.year = year
        self.marka = marka
        self.engine = engine
        self.color = color


    def drive(self, km):
        if self.engine < km//4:
            raise 'not enough fuel'
        a = km//4
        self.engine -= a
        print(f'waisted {a} fuel')

    def zapravka(self, fuel):
        self.engine += fuel

matiz = Car(2005, 'matiz', 5, 'red')
matiz.drive(20)
matiz.zapravka(6)

print(matiz.engine)


class Supercar(Car):
    def __init__(self, year, marka, engine, color, turbina):
        super().__init__(year, marka, engine, color)
        self.turbina = turbina


    def drive(self, km):
        if self.engine < km//2:
            raise 'not enough fuel'
        a = km//2
        self.engine -= a
        print(f'waisted {a} fuel')

#это полиморфизм, поменяли у родителя значение 4 на 2, переписание функции родителя дочкой
    def turnradio(self):
        print('radio')
#используем дочку и добалвяем турбину
ferrari = Supercar(2020, 'ferrari', 20, 'red', 10)

#matiz.turbina? нет турбины, потому в род классе

ferrari.turnradio()
ferrari.drive(20)

#ПОЛИМОРФИЗМ - измененение у дочки

