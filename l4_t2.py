# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
# Результаты анализа сохранить в виде комментариев в файле с кодом.
import cProfile
import timeit

n = 15


# Без использования «Решета Эратосфена»;
def no_eratosthenes(number):
    result_list = []
    while len(result_list) < number:
        for i in range(0, number * number):
            count = 0
            for y in range(1, i + 1):
                # print(f"i = {i}, y = {y}")
                if i % y == 0:
                    count += 1
                else:
                    pass
            if count == 2:
                result_list.append(i)
    return result_list[number - 1]


def main_no_eratosthenes():
    for _ in range(1000):
        no_eratosthenes(n)


print(f'простое число под номером {n} = {no_eratosthenes(n)} (без использования решетки эрастофена')
print(
    f'время затраченное на 1000 вызовов без использования решетки эрастофена - {timeit.timeit(f"no_eratosthenes({n})", globals=globals(), number=1000)}')
print('1000 вызовов для просмотра пролайфера')
cProfile.run('main_no_eratosthenes()')
# простое число под номером 15 = 47 (без использования решетки эрастофена
# время затраченное на 1000 вызовов без использования решетки эрастофена - 0.6509629
# 1000 вызовов для просмотра пролайфера
#          51004 function calls in 0.661 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.661    0.661 <string>:1(<module>)
#      1000    0.658    0.001    0.661    0.001 l4_t2.py:13(no_eratosthenes)
#         1    0.000    0.000    0.661    0.661 l4_t2.py:29(main_no_eratosthenes)
#         1    0.000    0.000    0.661    0.661 {built-in method builtins.exec}
#      2000    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     48000    0.003    0.000    0.003    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Используя алгоритм «Решето Эратосфена»
def eratosthenes(number):
    numbers_list = [i for i in range(2, number * number)]

    for i in numbers_list:
        for j in numbers_list:
            if j % i == 0 and i != j:
                numbers_list.pop(numbers_list.index(j))

    return numbers_list[number - 1]


def main_eratosthenes():
    for _ in range(1000):
        eratosthenes(n)


print(f'простое число под номером {n} = {eratosthenes(n)} (с использованием решетки эрастофена)')
print(
    f'время затраченное на 1000 вызовов без использования решетки эрастофена - {timeit.timeit(f"eratosthenes({n})", globals=globals(), number=1000)}')
print('1000 вызовов для просмотра пролайфера')
cProfile.run('main_eratosthenes()')
# простое число под номером 15 = 47 (с использованием решетки эрастофена)
# время затраченное на 1000 вызовов без использования решетки эрастофена - 0.1492388
# 1000 вызовов для просмотра пролайфера
#          352004 function calls in 0.199 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.199    0.199 <string>:1(<module>)
#      1000    0.098    0.000    0.198    0.000 l4_t2.py:41(eratosthenes)
#      1000    0.004    0.000    0.004    0.000 l4_t2.py:42(<listcomp>)
#         1    0.000    0.000    0.199    0.199 l4_t2.py:52(main_eratosthenes)
#         1    0.000    0.000    0.199    0.199 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    175000    0.078    0.000    0.078    0.000 {method 'index' of 'list' objects}
#    175000    0.019    0.000    0.019    0.000 {method 'pop' of 'list' objects}
