# Создайте класс Car. Пропишите в конструкторе параметры make, model, year,
# odometer, fuel. Пусть у показателя odometer будет первоначальное значение 0,
# а у fuel 70. Добавьте метод drive, который будет принимать расстояние в км. В
# самом начале проверьте, хватит ли вам бензина из расчета того, что машина
# расходует 10 л / 100 км (1л - 10 км) . Если его хватит на введенное расстояние,
# то пусть этот метод добавляет эти километры к значению одометра, но не
# напрямую, а с помощью приватного метода __add_distance. Помимо этого
# пусть метод drive также отнимет потраченное количество бензина с помощью
# приватного метода __subtract_fuel, затем пусть распечатает на экран “Let’s
# drive!”. Если же бензина не хватит, то распечатайте “Need more fuel, please, fill
# more!”
# Посмотреть задание


class Car:
    def __init__(self, make, model, year, odometer = 0, fuel = 70):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = odometer
        self.fuel = fuel

    def drive(self, distance):
        fuel = distance / 10
        if self.fuel >= fuel:
            self.__add_distance(distance)
            self.__subtract_fuel(fuel)
            print('Let’s drive!')
        else:
            print('Need more fuel, please, fill more!')

    def __add_distance(self, distance):
        self.odometer += distance

    def __subtract_fuel(self, fuel):
        self.fuel -= fuel

