names = ['Grey','Brown','Shephard']
numbers = ['123','234','678']
contacts = []
while True:
    print("\n--- Список контактов ---")
    print("1. Добавить контакт")
    print("2. Изменить контакт")
    print("3. Удалить контакт")
    print("4.Выход из программы")

    choice = input("Выберите действие: ")

    # Добавление контакта
    if choice == '1':
        name = input("Введите имя контакта: ")
        check = False
        if name in names:
            print("Имя контакта уже занято")
            check = False
        else:
            check = True
            names.append(name)
        number = input("Введите номер телефона контакта: ")
        if number in numbers:
            check = False
            print("Контакт уже существует ")
        else:
            numbers.append(number)
            check = True
        if check == True:
            contacts.append([names, numbers])
            print('Контакт успешно добавлен')



  # Изменение контакта
    if choice == '2':
        name = input("Введите имя контакта для изменения: ")
        check = False
        if name in names:
            print('5.Хотите изменить имя контакта?\n''6.Хотите изменить номер контакта?')
            choice = input("Выберите действие: ")
        elif name not in names:
            print('Контакт с таким именем не найден ')
    if choice == '5':
        new_name = input('Введите новое имя ')
        names.append(new_name)
        names.remove(name)
        print("Имя контакта изменено ")
    elif choice == '6':
        new_number = input('Введите новый номер ')
        numbers.append(new_number)
        numbers.remove(number)
        print("Номер контакта изменен ")

    # Удаление контакта
    if choice == '3':
        name = input("Введите имя контакта для удаления: ")
        if name in names:
            names.remove(name)
            print("Контакт успешно удален.")
        else:
            print("Контакт с таким именем не найден.")

    # Выход из программы:
    if choice =='4':
        print("Выход из программы")
        break
