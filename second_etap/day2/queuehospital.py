#Электронная очередь в поликлинике. Талоны, очередь, айди, и тд

import random
##данная функция включает рандом
import datetime
##этот модуль включает время
class Patient:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.created_date = datetime.datetime.now()
        print(self.created_date)
        #это время когда клиент был зарегестрирован, текущее время регистрирует
        self.end_date = None
        #когда закончится не знаем поэтому нон
        self.id = random.randint(0, 10000)
        #self.id - рандомно присваивает число от 0 до 10000


    def remove(self):
        self.end_date = datetime.datetime.now()
        #это время когда закончилось
        return f'вы ждали свою очередь - {self.end_date - self.created_date}'
    # показывает сколько человек ждал

    def check_info(self):
        if self.end_date:
            return f'человек по имени - {self.first_name} {self.last_name}\n в очереди - {self.end_date - self.created_date}'
        return f'человек по имени - {self.first_name} {self.last_name}\n в очереди - {self.end_date - datetime.datetime.now()}'


#нужно создать еще один класс для очереди
class Queue:
    def __init__(self):
        self.patients = []
        #пустой пациент, тут лежат пациенты, они должны быть класса Пациент
    def get_active_patients(self):
        return len([i for i in self.patients if not i.end_date])
    # сколько всего пациентов в очереди (активных)
    # если end_date не правда то значит это настоящие активные пациенты,
    # в противном случае мы его убираем ищ очереди. у не активынх пациентов
    # уже есть end_date

    def get_inactive_patients(self):
        return len([i for i in self.patients if i.end_date])
    #те пациенты у кого есть end_date

    def add_patient(self, patient: Patient):
        self.patients.append(patient)
        #добавить пациента

    def remaining(self, ticket):
        for i in range(len(self.patients)):
            if self.patients[i].id == ticket:
                return i * 10
        return 'there is no your ticket'

    def get_time_info(self, ticket):
        for i in range(len(self.patients)):
            if self.patients[i].id == ticket:
                return  self.patients[i].check_info

    def close_ticket(self, ticket):
        for i in range(len(self.patients)):
            if self.patients[i].id == ticket:
                return  self.patients[i].remove



