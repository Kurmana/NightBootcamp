class House:
    def __init__(self, doors, rooms, price, s=10):
        self.doors = doors
        self.rooms = rooms
        self.price = price
        self.s = s

    def add_new_door(self):
        self.doors += 1

    def get_keys_rooms(self):
        return list(self.rooms.keys())

    def remove_doors(self, col=1):
        self.doors -= col

    def __str__(self):
        return f'Дверей - {self.doors}\nКомнат - {self.rooms}'

    def __add__(self, other):
        return other.price + self.price


artemshome = House(8, 5, 50000, s=6)
dastanshome = House(6, 5, 20000, 4)

print(artemshome.__dir__())