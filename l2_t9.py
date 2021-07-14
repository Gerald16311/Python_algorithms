# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму
# его цифр.
numbers_list = input("Введите список натуральных чисел, разделенных пробелом - ")

while len(numbers_list) != 0:
    number = numbers_list[0: numbers_list.index(" ")]
    numbers_sum = 0
    for i in number:
        numbers_sum += int(i)
    numbers_list = numbers_list[numbers_list.index(" ")+1:]
    print(f"число выдернутое из списка - {number}, сумма - {numbers_sum}")
    print(f"оставшийся список - {numbers_list}")
