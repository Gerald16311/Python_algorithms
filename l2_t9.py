# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму
# его цифр.
numbers_list = input("Введите список натуральных чисел, разделенных пробелом - ")

# Решение без списков...
max_number, max_number_sum = 0, 0
while len(numbers_list) != 0:
    number = numbers_list[0: (numbers_list.find(" ")) if numbers_list.find(" ") != -1 else (len(numbers_list))]
    numbers_sum = 0
    for i in number:
        numbers_sum += int(i)
    numbers_list = numbers_list[numbers_list.find(" ") + 1:] if numbers_list.find(" ") != -1 else ""
    max_number = int(number) if numbers_sum > max_number_sum else max_number
    max_number_sum = numbers_sum if numbers_sum > max_number_sum else max_number_sum
    print(f"число выдернутое из списка - {number}, сумма - {numbers_sum}")
print(f'самая большая сумма цифр - число - {max_number} - сумма цифр -  {max_number_sum} ')

# Решение с исполоьзованием списка.....

# user_list = numbers_list.split(" ")
# numbers_list_sum = []
#
# for i in user_list:
#     numbers_sum = 0
#     for y in i:
#         numbers_sum += int(y)
#     numbers_list_sum.append(numbers_sum)
#
# print(f"Самая большая сумма цифр среди введеных чисел - {user_list[numbers_list_sum.index(max(numbers_list_sum))]}, "
#       f"сумма - {max(numbers_list_sum)}")
