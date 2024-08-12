my_dict = {'names': ['Jordan','Pavel','Sasha'],'user':'Pasha','numbers': (98, 80)}
print(my_dict)

#Методы словарей
instructor = {'names': ['Jordan','Pavel','Sasha'],'user':'Pasha','numbers': (98, 80)}
#values()- выдаст значение всех ключей
#keys() - выдаст ключи
#items() - выдаст ключи + значения
print(instructor.values())
print(instructor.keys())
a = list(instructor.values())
print(type(a))

instructor = {'name':"Jordan",'age':'21','job':'programmer'}
if 'name' in instructor:
    print('Yes')
else:
    print('No')

instructor = {'name':"Jordan",'age':'21','job':'programmer'}
if 21 in instructor.items():
    print('Yes')
else:
    print('No')

instructor = {'name':"Jordan",'age':'21','job':'programmer'}
instructor['gender'] = 'male'
print(instructor)

cafees = {'Evos':{'Gorod':"Tashkent",'Filialov':'Many',"Otkritie":'2007'}}
cafees['Evos']['кухня'] = 'Fastfood'
print(cafees)

instructor = {'name':"Jordan"}
instructor['name'] = [instructor['name'],'Pasha']
print(instructor)
instructor['name'].append('Oleg')
print(instructor)

# Методы для удаления
my_dict = {'song':'Godzilla','singer':'Eminem'}
#.clear - удалить все из словаря
#my_dict.clear()
print(my_dict)
#my_dict.popitem()
print(my_dict)
my_dict.pop('song')
print(my_dict)

#Методы для словарей
a = {}.fromkeys([1,2,3,4,5],0)
print(a)
print(a.get(5))
print(a.get(6))

a = dict(name = 'Jordan', age = 12)
print(a)
b = a.copy()
print(b)

#Сеты - набор неповторяющихся значений, не имеет индексов. Не работают методы
nums = {1,2,3,4,5,6,7,8,8,8,8,8,8,8,'g','r','r','t','yh','d','f'}
nums2 = set(nums)
print(nums2)

instructor = {'name':"Jordan",'age':'21','job':'programmer'}
for k,v in instructor.items():
    print(k,v)

inventory = {}
product_name = input("Введите название продукта: ")
quantity = int(input("Введите количество продукта: "))
inventory[product_name] = quantity


for product_name, quantity in inventory.items():
    print(f"{product_name}: {quantity}")

while True:
    command = input("Введите команду (добавить/продукты/выход): ")

    if command == "добавить":

    elif command == "продукты":
        show_products()
    elif command == "выход":
        break
    else:
        print("Неизвестная команда.")