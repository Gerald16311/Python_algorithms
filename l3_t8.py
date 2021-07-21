# Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму
# введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную
# матрицу.
import sys
matrix = []

for i in range(1,5):
    row = input(f'введите 4 элемента {i} строки матрицы - ').split(" ")
    if len(row) != 4:
        print('слишком много/мало чисел')
        print('необходимо вводить 4 числа, разделенные знаком пробел')
        sys.exit()
    else:
        matrix.append(row)

for row in matrix:
    items_summ = 0
    for item in row:
        items_summ += int(item)
    row.append(str(items_summ))

for i in matrix:
    print(*i)
