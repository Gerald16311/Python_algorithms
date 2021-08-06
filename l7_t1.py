# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в
# виде функции. По возможности доработайте алгоритм (сделайте его умнее).
import random
# СОздание массива случайных чисел
numbers_list = []
numbers_in_list = 10 # определение количства значений в массиве

for i in range(numbers_in_list):
    numbers_list.append(random.randint(-100, 100))
print(numbers_list) #вывод массива на экран


# функция сортировки исходного массива от большего к меньшему
def sorting():
    for i in range(len(numbers_list) - 1):
        for j in range(len(numbers_list) - i - 1):
            if numbers_list[j] < numbers_list[j + 1]:
                numbers_list[j], numbers_list[j + 1] = numbers_list[j + 1], numbers_list[j]

#вызов функции
sorting()
#вывод на экран полученного результата
print(numbers_list)
