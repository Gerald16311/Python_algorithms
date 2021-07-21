# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например,
# если введено число 3486, то надо вывести число 6843.

number = str(int(input("Введите натуральное число - ")))


# 1 вариант решения через цикл
# result = ""
# for i in range(len(number), 0, -1):
#     result += number[i - 1]
#
# print(f"Результат - {result}")

# 2 вариант через срез
# result = number [::-1]
# print(f"Результат - {result}")

# 3 вариант с помошью рекурсии
def recursion(n):
    if len(str(n)) == 1:
        return str(n)
    else:
        return str(n % 10) + str(recursion(n // 10))


print(recursion(int(number)))
