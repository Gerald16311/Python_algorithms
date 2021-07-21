# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами
# минимальный и максимальный элементы в сумму не включать.

from random import randint

lst = [randint(-100000, 100000) for i in range(100)]

items_summ = 0
for i in range(lst.index(min(lst)) + 1, lst.index(max(lst))):
    items_summ += i

print(f'Сумма элементов между самым большим и маленьким числом = {items_summ}')
