# Функция добавления клиента
# Словарь с клиентами и номерами комнат
clients = {}
def добавить_клиента():
    # Вывести список занятых номеров
    print("Занятые номера:")
    for name, number in clients.items():
        print(f"- {name}: {number}")

    # Ввести имя клиента и номер комнаты
    name = input("Введите имя клиента: ")
    number = input("Введите номер комнаты: ")

    # Добавить клиента в словарь
    клиенты[name] = number
    print(f"Клиент {name} добавлен в номер {number}")

# Функция удаления клиента
def удалить_клиента():
    # Ввести имя клиента для удаления
    name = input("Введите имя клиента для удаления: ")

    # Удалить клиента из словаря
    if name in clients:
        del clients[name]
        print(f"Клиент {name} удален")
    else:
        print("Клиент не найден")

# Функция отображения занятых номеров
def показать_занятые_номера():
    # Вывести список занятых номеров
    print("Занятые номера:")
    for number, name in clients.items():
        print(f"- {number}: {name}")

# Цикл для взаимодействия с пользователем
while True:
    # Вывести меню
    print("Выберите действие:\n 1. Добавить клиента \n 2. Удалить клиента \n 3. Показать занятые номера\n 4. Выход")

    # Ввести номер действия
    choice = input("Введите номер действия: ")

    # Выполнить действие в зависимости от выбора пользователя
    if choice == "1":
        добавить_клиента()
    elif choice == "2":
        удалить_клиента()
    elif choice == "3":
        показать_занятые_номера()
    elif choice == "4":
        break
    else:
        print("Неверный выбор")