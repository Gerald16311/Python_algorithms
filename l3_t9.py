# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import randint
lst = [randint(0, 100) for i in range(100)]


collums = int(input('Введите количество столбцов в генерируемой матрице - '))
rows = int(input('Введите количество строк в генерируемой матрице - '))
min_number = int(input('Введите минимальное число матрицы - '))
max_number = int(input('Введите максимальное число матрицы - '))
matrix = []

for i in range (1, rows+1):
    row = [randint(min_number, max_number) for y in range(collums)]
    matrix.append(row)

# for i in matrix:
#     print(*i)

min_numbers_list = []

for i in range(0, collums):
    min_number_in_collum = matrix[0][i]
    for y in range(0, rows):
        if matrix[y][i] < min_number_in_collum:
            min_number_in_collum = matrix[y][i]
        else:
            pass
    min_numbers_list.append(min_number_in_collum)
    # print(f'Самое маленькое число в {i+1} колонке - {min_number_in_collum}')

print(f'Самое большое число среди самых маленьких в коллонке - {max(min_numbers_list)}')