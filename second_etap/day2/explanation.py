class Human:
    #метод для создания экземпляра"""
    def __init__(self, first_name, last_name, occupation, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.occupation = occupation
        self.age = age
        self.sex = sex
        print('I was born')

    def change_name(self, new_name):
        self.first_name = new_name
    #метод по замене имени

    def birthday(self):
        self.age += 1
    #метод для добавления возраста. обрати внимание что только self


a = Human('Aichurek', 'Kurmanbekova', 'reposrting officer', 33, 'female')
b = Human('Aiganysh', 'Asanalieva', 'project manager', 31, 'female')

print(a.first_name)
a.change_name('Aichu')
print(a.first_name)

a.birthday()
print(a.age)
