import psycopg2

# открываем соеденение с бд, не забудь обновить user какое имя в бд
conn = psycopg2.connect('dbname=youtube user=Aichurek')

# создаем посредника "курсор"
cur = conn.cursor()

# #передаем запрос курсору (qwery - zapros)
# cur.execute('SELECT * FROM users')
#
# # он выполняет и возращает ответ
# total = cur.fetchall()
#
# for i in total:
#     print(f'имя {i[1]}\nВозраст - {i[2]}\nХобби - {i[3]}')



while True:
    print('1 - список студентов\n2 - добавить студентов\n3 - посик студентов по имени\n4 - удаление студентов через id')
    choice = int(input())
    if choice == 1:
        cur.execute('select * from users')
        for i in cur.fetchall():
            print(f'ID - {i[0]}\nимя {i[1]}\nВозраст - {i[2]}\nХобби - {i[3]}')
    elif choice ==2:
        first_name = input()
        last_name = input()
        age = input()
        hobby = input()
        cur.execute(f'insert into users(name, last_name, age, description) values ("{first_name}", "{last_name}", "{age}", "{hobby}")')
        conn.commit()
        print('success')
    elif choice == 3:
        name = input('Search by first_name')
        cur.execute(f'select * from users where  name like "{name}%"')
        for i in cur.fetchall():
            print(f'ID - {i[0]}\nимя {i[1]}\nВозраст - {i[2]}\nХобби - {i[3]}')
    elif choice == 4:
       id = input()
       cur.execute(f'delete from users where id = {id}')
       conn.commit()
       print('success')
    else:
        print('error')
