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


print(f"1 Результат (цикл) - {first_result(number)}")
print(timeit.timeit(first_result(number)))
cProfile.run('first_result(number)')

# 1 Результат (цикл) - 987654321
# 0.0058531
#          5 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 l4_t1.py:11(first_result)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# 2 вариант через срез
def slised(n):
    result = number[::-1]
    return result


print(f"2 Результат (срез) - {slised(number)}")
print(timeit.timeit(slised(number)))
cProfile.run('slised(number)')

# 2 Результат (срез) - 987654321
# 0.006168800000000002
#          4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 l4_t1.py:24(slised)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# 3 вариант с помошью рекурсии
def recursion(n):
    if len(str(n)) == 1:
        return str(n)
    else:
        return str(n % 10) + str(recursion(n // 10))


print(f"3 Результат (рекурсия)- {recursion(int(number))}")
print(timeit.timeit(recursion(int(number))))
cProfile.run('recursion(int(number))')

# 3 Результат (рекурсия)- 987654321
# 0.005613100000000003
#          21 function calls (13 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#       9/1    0.000    0.000    0.000    0.000 l4_t1.py:35(recursion)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         9    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
