# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a, b, c = [int(i) for i in input("Введите три числа = ").split()]

numbers_list = [a, b, c]
numbers_list.sort()
print(f"Среднее число = {numbers_list[1]}")