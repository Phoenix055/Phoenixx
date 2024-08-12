# Сценарии использования list comprehension.
# 1. Создания списка с отфильтрованными элементами: Числа делящиеся на 6
# 2. Создание списков с несколькими условиями
nums1 = [i for i in range(1,50)]
nums2 = [num for num in nums1 if num % 2 == 0 and num % 3 == 0]
print(nums1)
print(nums2)

# 3. Математические функции
cubes = [x ** 3 for x in range(3,17,3)]
print(cubes)

# 4. Генерация списка с использованием диапозонов
wed = [i for i in range(1,100,20)]
print(wed)

# 5. Создание списка с преобразованными элементами:
vegs = ['pumbkin','pickle','potato','tomato','carrot']
vegs2 = [len(x) for x in vegs]
print(vegs2)

# 6. Видоизмененные список из другого списка
names = ['Masha', "Oleg", "Pavel"]
name = [x.lower() for x in names]
print(name)

#7. Вложенные списки
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
grid2 = [x for row in grid for x in row]
print(grid2)