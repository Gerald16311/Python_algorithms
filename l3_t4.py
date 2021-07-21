# Определить, какое число в массиве встречается чаще всего.

from random import randint
lst = [randint(0, 100) for i in range(100)]

count = 0
number = 0
for i in lst:
    if lst.count(i) > count:
        count = lst.count(i)
        number = i
    else:
        pass

print(f'чаще всего в случайно сгенерированным списком встречается {number} - стречается {count} раз')