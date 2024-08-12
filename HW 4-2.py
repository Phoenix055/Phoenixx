#Числа от 1 до 100:
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Убрать дубликаты в списке
list1 = [1, "hello", True, [1, 2, 3], 2.5, 1, "world", False, [4, 5, 6], 3.5, 3, "foo", True, [7, 8, 9], 4.5, 4, "bar", False, [10, 11, 12], 5.5, 5, "baz", True, [13, 14, 15], 6.5, 1, "hello", True, [1, 2, 3], 2.5,1, "world", False, [4, 5, 6], 3.5, 3, "foo", True, [7, 8, 9], 4.5,4, "bar", False, [10, 11, 12], 5.5, 5, "baz", True, [13, 14, 15], 6.5, 6, "hello", False, [16, 17, 18], 7.5, 7, "world", True, [19, 20, 21], 8.5, 8, "foo", False, [22, 23, 24], 9.5, 9, "bar", True, [25, 26, 27], 10.5, 10, "baz", False, [28, 29, 30], 11.5, 6, "hello", False, [16, 17, 18], 7.5, 7, "world", True, [19, 20, 21], 8.5, 8, "foo", False, [22, 23, 24], 9.5, 9, "bar", True, [25, 26, 27], 10.5, 10, "baz", False, [28, 29, 30], 11.5]
list = []
for x in list1:
    if x not in list:
        list.append(x)
        print(list)
