#Списки в пайтоне - массивы. Массив - это один элемент. Являются изменяемой структурой.
# Списки создаются с помощью квадратных скобок []
a=[12,343546.436,'Glory',['Memory']]  #Список с разными элементами
# len()- количество переменных
a = [1,2,2,3,4,['Flight']]
print(len(a))
print(type(a))
#Доступ к элементам осуществляется через индексы 0,1,2,3... и отриц индекс -1,-2,-3 если с конца листа
#List Slicing - делим лист на кусочки(слайсы).
list = [12,34,'Only',[1,2,3,4,5],234]
print(list[1])
print(list[1:3])
print(list[0:3:1])

#Методы добавления в лист
name1 = [1,2,3,4,5]
name2 = name1[ : :-1]
print(name2)
print(name1)

#Элементы сами состоят из элементов
words = ['Ceremony','Serendipity','Inquiry']
print(words[1][2:5])

#Методы для добавления
#.append - добавление элементов в конец
word1 = ['Side']
word1.append('walk')
print(word1)
#insert - добавление в определенное место по индексу
words = ['Superman','Hulk','Captain America']
words.insert(1,'Batman')
print(words)
#extend - слияние списков конец в конец
words = ['Superman','Hulk','Captain America']
words.extend(['Wonder Woman', 'Joker','Batman'])
print(words)
#Методы для удаления
#.clear - удаление всех элементов, остается сам список
words = ['Superman','Hulk','Captain America']
words.clear()
print(words)
#pop - удаление последнего элемента списка либо по индексу элемента
words = ['Superman','Hulk','Captain America']
words.pop(1)
print(words)
#remove - удаление элемента по значению, не по индексу
words = ['Superman','Hulk','Captain America']
words.remove('Captain America')
print(words)

#Методы для изменения
words = ['Superman','Hulk','Captain America']
#name[индекс элемента, которого хотим изменить]
words[1] = 'Wonder Woman 2'
print(words)
#Сортировка по алфавиту
words = ['Superman', 'Hulk', 'Captain America', 'Wonder Woman', 'Joker', 'Batman']
words.sort()
print(words)
#Сортировка обратная
words = ['Superman', 'Hulk', 'Captain America', 'Wonder Woman', 'Joker', 'Batman']
words.reverse()
print(words)
#Найти индекс по значению
words = ['Superman', 'Hulk', 'Captain America', 'Wonder Woman', 'Joker', 'Batman']
words_index = words.index('Hulk')
print(words_index)

#Кортежи - tuples. Те же самые списки, только невозможно менять ничего и образуются с помощью ()
Mein = ('ich', )
print(type(Mein))
Mein = 'ich',
print(type(Mein))

#Оператор in для проверки на наличие элементов с помощью условных операторов
words = ['Superman', 'Hulk', 'Captain America', 'Wonder Woman', 'Joker', 'Batman']
if 'Joker' in words:
    print('DC comics')
elif 'Captain America' in words:
    print('is not Marvel')
else:
    print('Mistake')

menu = input("Выберие дейтсвие:")
name = input("Введите имя гостя : ")
room_number = input("Введите номер комнаты гостя: ")
guests = []
guests.append([name, room_number])
print(guests)


