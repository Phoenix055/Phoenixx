#Цикл-многократное повторяющееся действие. Два вида while and for. Могут друг друга имитировать
#For- работает по элементам, проверяет каждый элемент
name = 'Pasha'
for item in name:
    print(item)

my_list = [1,'a',4.5]
for spam in my_list:
    print(spam)
#Функция range используется, чтобы задать количество повторений
my_tuple = (6,4,'2')
for i in range(1,100):
    print(f'{my_tuple}')


p =['m','12','23.4']
for thor in p:
    print(thor)

massive = [10,30,50,60,70]
count = 0
for i in massive:
    count += 1
print(count)

#my_list = (6,4,'2')
#for t in my_list:
    #print(t+2)

#range - итерация, или повторение
my_list = ('2',4,'3')
for t in range(1,100):
    print(t)

#While - бесконечный цикл сTrue
p = ['m','my',23]
i= 0
while i<len(p):
    print(p[i])
    i = i+1
for i in p:
    print(i)

names = ['Ivan','Pavel','Jordan']
while True:
    new = input('Кого добавить?')
    if new =='Список':
        print(names)
    else:
        names.append(new)
        print(f'{new}добавлен')

names = []
numbers = []
services = []
while True:
    menu = input("Что хотите сделать?\n\n"
                 "1- Добавить имя\n"
                 "2- Добавить номер\n"
                 "3- Добавить услугу\n"
                 "4- Посмотреть списки\n"
                 "5- Выход\n"
                 "______________________\n")
    if menu == "1":
        name = input("Введите имя: ")
        if name in names:
            print("Имя занято")
        else:
            names.append(name)
    elif menu == "2":
        number = input("Введите номер: ")
        if number in numbers:
            print("Номер занят")
        else:
            numbers.append(number)
    elif menu == "3":
        service = input("Введите услугу: ")
        if service in services:
            print("Услуга уже существует")
        else:
            services.append(service)
    elif menu == "4":
        what = input("Какой список хотите глянуть?: ")
        if what == "имен":
            count = 0
            for i in names:
                count += 1
                print(f"{count}. {i}")
        elif what == "номеров":
            count = 0
            for i in numbers:
                count += 1
                print(f"{count}. {i}")
        elif what == "услуг":
            count = 0
            for i in services:
                count += 1
                print(f"{count}. {i}")
    elif menu == "5":
        print("Программа закрыта")
        break
