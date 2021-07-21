# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба
# являться минимальными), так и различаться.
from random import randint

lst = [randint(-100000, 100000) for i in range(10)]
lst2 = lst
print(lst)
min_number_index = lst.index(min(lst))
print(f'1 минимальный элемент массива = {lst[min_number_index]}')

lst2.pop(min_number_index)
print(lst2)
print(f'2 минимальный элемент массива = {min(lst2)}')