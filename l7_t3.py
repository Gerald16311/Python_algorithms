# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком
# сложно, то используйте метод сортировки, который не рассматривался на уроках
import random, statistics

# Создание массива случайных чисел
numbers_list = []
numbers_in_list = 5  # определение размера массива

for i in range(2 * numbers_in_list + 1):
    numbers_list.append(random.randint(0, 50))
print(f"Исходный массив - {numbers_list}")  # вывод массива на экран
print(f"Медиана с помощью модуля statistics - {statistics.median(numbers_list)}")

poped_list = numbers_list #дополнительный список который будет модифицироваться в цикле
for i in range(0,numbers_in_list):
    max_number = max(poped_list)
    poped_list.pop(poped_list.index(max_number))

print(f"медиана найденая мной - {max(poped_list)}")
