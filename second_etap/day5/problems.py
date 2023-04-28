# class Student:
#     def __init__(self, name, group):
#         self.name = name
#         self.group = group
#
#     def __del__(self):
#         print('bye bye')


class Student:

    def __init__(self, name, final_exam):
        self.name = name
        self.final_exam = final_exam
        self.mydict = {}

    def make_lab(self, m, n):
        return self
    #return self - возвращает ссылку на текущий объект

    def make_exam(self, m):
        return self

    def is_certified(self, m):
        if m >= 0.61:
            print('pass')
        else:
            print('fail')

            return tuple(sum(m))



a = Student('Alex', {'exam_max': 30})
b = Student('Sakurai', {'lab_max', 7})
c = Student('Watanabe', {'lab_num', 10})
d = Student('Haruka', {'k', 0.61})



