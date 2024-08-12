contacts = []
print("\n--- Список контактов ---")
print("1. Добавить контакт")
print("2. Изменить контакт")
print("3. Удалить контакт")

choice = input("Выберите действие: ")

# Добавление контакта
if choice == '1':
    name = input("Введите имя контакта: ")
    number = input("Введите номер телефона контакта: ")
    contacts.append([name, number])
    print('Контакт успешно добавлен')
elif name and number in contacts:
    print('Имя контакта уже занято')

# Изменение контакта
if choice == '2':
    name = input("Введите имя контакта для изменения: ")
    if name and number in contacts:
        new_number = input("Введите новый номер телефона: ")
        if number != new_number:
            print("Номер телефона контакта успешно изменен.")
        else:
            print("Контакт с таким именем не найден.")

# Удаление контакта
if choice == '3':
    name = input("Введите имя контакта для удаления: ")
    if name in contacts:
        name.clear()
        print("Контакт успешно удален.")
    else:
        print("Контакт с таким именем не найден.")