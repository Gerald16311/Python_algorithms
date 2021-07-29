# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых
# трех уроков. Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
import timeit, cProfile

# Урок 2 задание 3

number = "123456789"


# 1 вариант решения через цикл
def first_result(n):
    result = ""
    for i in range(len(n), 0, -1):
        result += n[i - 1]
    return result


def main_first_result():
    for _ in range(1000):
        first_result(number)


print(f"1 Результат (цикл) - {first_result(number)}")
print(timeit.timeit(first_result(number), number=1000))
cProfile.run('main_first_result()')


# 1 Результат (цикл) - 987654321
# 5.700000000000843e-06
#          2004 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#      1000    0.001    0.000    0.001    0.000 l4_t1.py:11(first_result)
#         1    0.000    0.000    0.001    0.001 l4_t1.py:18(main_first_result)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#      1000    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# 2 вариант через срез
def slised(n):
    result = n[::-1]
    return result


def main_slised():
    for _ in range(1000):
        slised(number)


print(f"2 Результат (срез) - {slised(number)}")
print(timeit.timeit(slised(number), number=1000))
cProfile.run('main_slised()')


# 2 Результат (срез) - 987654321
# 8.30000000000275e-06
#          1004 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1000    0.000    0.000    0.000    0.000 l4_t1.py:29(slised)
#         1    0.000    0.000    0.000    0.000 l4_t1.py:34(main_slised)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# 3 вариант с помошью рекурсии
def recursion(n):
    if len(str(n)) == 1:
        return str(n)
    else:
        return str(n % 10) + str(recursion(n // 10))


def main_recursion():
    for _ in range(1000):
        recursion(int(number))


print(f"3 Результат (рекурсия)- {recursion(int(number))}")
print(timeit.timeit(recursion(int(number)), number=1000))
cProfile.run('main_recursion()')


# 3 Результат (рекурсия)- 987654321
# 5.499999999998562e-06
#          18004 function calls (10004 primitive calls) in 0.007 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.007    0.007 <string>:1(<module>)
# 9000/1000    0.006    0.000    0.006    0.000 l4_t1.py:45(recursion)
#         1    0.000    0.000    0.007    0.007 l4_t1.py:52(main_recursion)
#         1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
#      9000    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
