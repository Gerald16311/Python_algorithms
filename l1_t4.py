# Написать программу, которая генерирует в указанных пользователем границах:
#       случайное целое число;
#       случайное вещественное число;
#       случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ
# от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f'
# включительно.

import random

input_number = int(input('Введите число от 1 до 3, в зависимсоти от того что надо сгенерировать "случайное целое число '
                         '- 1", "случайное вещественное число - 2" или  "случайный символ - 3" '))

if 1 <= input_number <= 3:
    if input_number == 1:
        x1, y1 = [int(i) for i in
                  input("Введите 2 целых числа между которыми необходимо получить случайное число = ").split()]
        print(f"Случайное целое число из диапазона от {x1} до {y1} - {random.randint(x1, y1)}")
    elif input_number == 2:
        x1, y1 = [float(i) for i in
                  input("Введите 2 вещественных числа между которыми необходимо получить случайное число = ").split()]
        print(f"Случайное вещественное число из диапазона от {x1} до {y1} - {random.uniform(x1, y1)}")
    else:
        x1, y1 = [str(i) for i in
                  input("Введите 2 символа между которыми необходимо получить случайный символ = ").split()]
        print(f"Случайный символ из диапазона от {x1} до {y1} - {chr(random.randint(ord(x1), ord(y1)))}")
else:
    print("Введено неверное число")
