from queuehospital import Patient
from queuehospital import Queue

def create_patient():
    first_name = input('enter your first name ')
    last_name = input('enter your last name ')
    age = input('enter your age ')
    patient = Patient(first_name, last_name, age)
    return patient

queue = Queue()

while True:
    print('Welcome to the Hospital')
    choice = input('yes or no, do you want to get a queue - \n')
    if choice.lower() == 'yes':
        patient = create_patient()
    # функция create_patient
        queue.add_patient(patient)
        print(f'вы успешно в очереди - ваш талон - {patient.id}')
    print('посмотреть сколько осталось времени - 1\nУзнать сколько времени я в очереди - 2\n сколько людей в очереди - 3 \n посмотреть инфу о талоне - 4\n закрыть талон - 5')
    choice = int(input('your choice - '))
    ticket = int(input('enter your ticket - '))
    if choice == 1:
        print(queue.remaining(ticket))
    elif choice == 2:
        print(queue.get_time_info(ticket))
    elif choice == 3:
        print(queue.get_active_patients())
    elif choice == 4:
        print(queue.close_ticket(ticket))



