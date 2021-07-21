# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint
lst = [randint(0, 100) for i in range(100)]

max_number = max(lst)
min_number = min(lst)
max_number_index = lst.index(max_number)
min_number_index = lst.index(min_number)

print(f'Самое большое число в списке {max_number} - с индексом {lst.index(max_number)}')
print(f'Самое маленькое число в списке {min_number} - с индексом {lst.index(min_number)}')
print('После замены мест')

lst[min_number_index] = max_number
lst[max_number_index] = min_number

print(f'Самое большое число в списке после смены мест {max_number} - с индексом {lst.index(max_number)}')
print(f'Самое маленькое число в списке после смены мест {min_number} - с индексом {lst.index(min_number)}')