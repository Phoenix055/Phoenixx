# Bottles
bottles_over_1_liter = int(input("Введите количеcтво бутылок меньше 1л: "))
bottles_under_1_liter = int(input("Введите количество бутылок больше 1л : "))

# Подсчет выгоды от бутылок.
revenue_over_1_liter = bottles_over_1_liter * 0.25
revenue_under_1_liter = bottles_under_1_liter * 0.10

# Общий доход.
total_revenue = revenue_over_1_liter + revenue_under_1_liter
print("The total revenue from all bottles is ${:.2f}".format(total_revenue))

# Payment at restaurant
Payment = float(input("Введите сумму заказа "))
Tips = Payment * 0.18
Tax = Payment * 0.12
Overall = Payment + Tips + Tax
print('Сумма для оплаты ${:.2f}'.format(Overall))

# Сумма натуральных чисел
number = int(input("Enter a number: "))
summa = 0
for i in range(1, number + 1):
    # Add the current number to the sum.
    summa = (i*(i+1))/2
print("The sum of the numbers from 1 to {} is {}".format(number, summa))

# Безделушки
souvenir = int(input("Введите количество сувениров: "))
toy = int(input("Введите количество безделушек : "))
# Подсчет массы
souvenir_mass = souvenir * 75
toy_mass = toy * 112
Overall_mass = toy_mass + souvenir_mass
print("Общая масса заказа {}гр".format(Overall_mass))
