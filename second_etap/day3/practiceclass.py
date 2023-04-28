# class Factory:
#     def __init__(self):
#         def engine(self):
#             return 'the engine is created'
#
#         def bridge(self):
#             return 'the moving part is created'
#
# class Toyota(Factory):
#
#     def wheels(self):
#         return 'wheels are ready'
#
#     def windows(self):
#         return 'windows are ready'
#
#
# a = Toyota()
# print(a.wheels())
# print(a.windows())


class Zoo:
    def __init__(self):
        self.animal_1 = 'tiger'
        self.animal_2 = 'hippopotamus'
        self.animal_3 = 'giraff'

    def change_animal(self):
        self.animal_1 = 'lion'
        self.animal_3 = 'snake'

        return self.animal_3, self.animal_1


z = Zoo()

z.animal_4 = [z.animal_3, z.animal_2]
print(z.animal_4)
z.change_animal()
print(z.change_animal())

