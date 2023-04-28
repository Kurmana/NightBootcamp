
# аттрибуты- кол-во мест, список машин[пустой] который принимает в себе
# объекты экземпляра класса car, записи - dictinary  {в котором будут все таллоны
# # и информация о том какая машина заехала икогда уехала, булиан которая обозначает
# находится на парковке машина или нет },  талоны должны быть сгенерированны рандомно
# и должны быть уникальны
# методы - 1. Вызывается addCar принимает в себя аргумент класса Car, метод должен
# добавить в наш аттрибут 'Машины' и добавляет новый элемент в записи талон и если
# машина не уехала, то поле когда уехала машина возвращает  none
# метод - 2 Вызывается out_car(«talon») вы ищите талон и в записях добавляете время
# выхода машины а также булиан ставите фалс о том что машины нет в парковке, а также
# удилите машину из списка Машины
# Добавьте также разные методы чтобы просмотреть детально запись о машине итд

import random
import datetime


class Car:
    def __init__(self, name_car, plate_number, type_car):
        self.name_car = name_car
        self.plate_number = plate_number
        self.type_car = type_car
        self.created_date = datetime.datetime.now()
        print(self.created_date)
        self.in_the_parking = True
        self.end_date = None
        self.id = random.randint(0, 100)

    #finished parking
    def remove(self):
        self.end_date = datetime.datetime.now()
        return f'the time of your parking is - {self.end_date - self.created_date}'

    #this method provides infor to a customer
    def check_info(self):
        if self.end_date:
            return f'your car {self.type_car} {self.plate_number}\n was in the parking for - {self.end_date - self.created_date}'
        return f'your car - {self.type_car} {self.plate_number}\n was in the parking - {self.end_date - datetime.datetime.now()}'

class Parking:
    def __init__(self):
        self.max_spots = 80
        self.in_the_parking = True
        self.cars = []


    def cars_in_the_parking(self):
        #will show how many cars are in the parking area
        return len([i for i in self.cars if not i.end_date])

    def car_not_in_parking(self):
        return len([i for i in self.cars if i.end_date])

    def confirmation(self, ticket):
        for i in self.cars:
            if i.id == ticket:
                #if i not in i.end_date:
                return f'Yes, the car is in the parking'

            else:
                return 'No, the car has left'

    def add_car(self, car: Car):
        self.cars.append(car)

    def remaining(self, ticket):
        for i in range(len(self.cars)):
            if self.cars[i].id == ticket:
                return i * 60
        return 'your car is not there'

    def get_time_info(self, ticket):
        for i in range(len(self.cars)):
            if self.cars[i].id == ticket:
                return self.cars[i].check_info()

    def total_number_of_the_cars(self):
        return len(self.cars)


    def close_ticket(self, ticket):
        for i in range(len(self.cars)):
            if self.cars[i].id == ticket:
                return self.cars[i].remove