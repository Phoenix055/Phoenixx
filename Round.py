#Принцип округления работает так, чтобы округлит до ближайшего четного числа
a = round(3.5) #'=4'
a = round(6.5) #'=6'

#Мы также можем указывать до какого числа нам округлять
b = round(34.3663463464, 4) #'=34.3663'
#Можем округлять в сторону целого числа
c = round(34647.3473437, -4) #'=30000.0'
print(c)

#Модули math В math.ceil все работает как в математике, округляет в сторону большего, неважно четное или нечетное неважно

import math
d = math.ceil(45.728) #'=46'
d = math.ceil(4.5) #'=5'
d = math.ceil(4.1) #'=5'
#Округление в меньшую сторону math floor
d = math.floor(-34.9) #'=-34'

#Отбрасывание дробной части - math.trunc
f = math.trunc (45.4263512781) #='45'
print(f)

