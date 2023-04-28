from test import Car
from test import Parking


def create_car():
    plate_number = input('enter the plate info of your car - ')
    name_car = input('enter your name - ')
    type_car = input('enter type of your car - ')
    car = Car(plate_number, name_car, type_car)
    return car

parking = Parking()

print('welcome to our car park!')
choice = input('press yes if you would like to park your car (the parking number will be generated authomatically),\notherwise press no\n')
if choice == 'yes':
    car = create_car()
    parking.add_car(car)
    print(f'please park your car at {car.id}')
elif choice == 'no':
    print('thank you for visiting us. bye bye!')
else:
    print('please enter yes or no only')


while True:
    print('to check time of your parking: press 1\nto check how many cars there are in the parking are: press 2\nto check out: press 3\nto get info about number of maximum spots in this car park press 4\nto check if your car is in the parking: press 5')
    choice = int(input('your choice - '))
    ticket = int(input('enter your ticket number - '))
    if choice == 1:
        print('remaining time', parking.remaining(ticket))
    elif choice == 2:
        print('there are/is', parking.cars_in_the_parking(), 'car(s) in the parking')
    elif choice == 3:
        print(parking.close_ticket(ticket), 'your ticket is closed, bye')
    elif choice == 4:
        print('there are', parking.max_spots, 'spots in total, however, not all of them are available')
    elif choice == 5:
        print(parking.confirmation(ticket))

    print('would you like to continue? please enter yes or no')
    choice1 = input('your choice - ')
    if choice1.lower() == 'yes':
        ticket = int(input('enter your ticket number - '))
    elif choice1.lower() == 'no':
        print('bye bye!')
    break





