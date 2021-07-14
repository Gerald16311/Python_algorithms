# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму
# его цифр.
numbers_list = input("Введите список натуральных чисел, разделенных пробелом - ")

# while len(numbers_list) != 0:
#     number = numbers_list[0: (numbers_list.find(" ")) if numbers_list.find(" ") != -1 else (len(numbers_list)-1)]
#     numbers_sum = 0
#     for i in number:
#         numbers_sum += int(i)
#     numbers_list = numbers_list[numbers_list.find(" ")+1:]
#     print(f"число выдернутое из списка - {number}, сумма - {numbers_sum}")
#     print(f"оставшийся список - {numbers_list}")

user_list = numbers_list.split(" ")
numbers_list_sum = []

for i in user_list:
    numbers_sum = 0
    for y in i:
        numbers_sum += int(y)
    numbers_list_sum.append(numbers_sum)

print(f"Самая большая сумма цифр среди введеных чисел - {user_list[numbers_list_sum.index(max(numbers_list_sum))]}, "
      f"сумма - {max(numbers_list_sum)}")

