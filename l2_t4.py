# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.

n = int(input("Введите число n - "))
number = 1
result = 1
for i in range(1, n, 1):
    number = number / (-2)
    # print(number)
    result += number
print(f"сумма элементов заданного ряда = {result}")


# с помошью рекурсии
# def recursion(n):
#     if n == 1:
#         return n
#     else:
#         print(1 / (n * (-2)))
#         return (1 / (n * (-2))) + recursion(n-1)
#
#
# print(f"сумма элементов заданного ряда = {recursion(n)}")