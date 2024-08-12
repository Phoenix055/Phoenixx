# List comprehension - функция создания новых листов
#[новая переменная for новая переменная in набор_значений]
nums = [1,2,3,4]
numbers2 = [spam * 2 for spam in nums]
print(numbers2)
#Условные операторы в List comprehension
nums = [i for i in range(1,11)]
chotnie = [num for num in nums if num % 2 == 0]
nechotnie = [num for num in nums if num % 2 != 0]
print(chotnie, nechotnie)

names = ['Pavel','Sasha','Jordan','Pasha']
answer = [name[0] for name in names]
print(answer)

list = [i for i in range (1,11,2)]
print(list)

nums1 = [i for i in range(1,20)]
nums2 = [num for num in nums1 if num % 2 == 0]
print(nums1)
print(nums2)

username = ['Oleg']
while True:
    menu = input("Введите имя ")
    if menu.lower() in [a.lower() for a in username]:
        print("Такой user имеется")
        print(username)
    else:
        username.append(menu)
        print("Username успешно добавлен")
        print(username)


list = [i for i in range (1,11,2)]
print(my_list)