# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
# Результаты анализа сохранить в виде комментариев в файле с кодом.
import cProfile
import timeit

n = 15


# Без использования «Решета Эратосфена»;
# Специально написал самый медленный алгоритм, с 2мя циклами
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
print(f'время затраченное на 1000 вызовов без использования решетки эрастофена - {timeit.timeit(f"no_eratosthenes({n})", globals=globals(), number=1000)}')
print('1000 вызовов для просмотра пролайфера')
cProfile.run('main_no_eratosthenes()')
# простое число под номером 15 = 47 (без использования решетки эрастофена
# время затраченное на 1000 вызовов без использования решетки эрастофена - 0.7255193999999999
# 1000 вызовов для просмотра пролайфера
#          51004 function calls in 0.648 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.648    0.648 <string>:1(<module>)
#      1000    0.645    0.001    0.648    0.001 l4_t2.py:13(no_eratosthenes)
#         1    0.000    0.000    0.648    0.648 l4_t2.py:29(main_no_eratosthenes)
#         1    0.000    0.000    0.648    0.648 {built-in method builtins.exec}
#      2000    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     48000    0.003    0.000    0.003    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Используя алгоритм «Решето Эратосфена»
# 1. Выписать все целые числа 2,...,N.
# 2. Пусть переменная p изначально равна двум — первому простому числу.
# 3. Зачеркнуть в списке числа от 2p до n считая шагами по p (это будут числа кратные p: 2p, 3p, 4p, …)
# 4. Найти первое незачёркнутое число в списке, большее чем p, и присвоить значению переменной p это число.
# 5. Повторять шаги 3 и 4, пока возможно.

def eratosthenes(number):
    sieve = set(range(2, number * number))
    result_list = []
    while sieve:
        prime = min(sieve)
        result_list.append(prime)
        sieve -= set(range(prime, number * number + 1, prime))
    return result_list[number - 1]


def main_eratosthenes():
    for _ in range(1000):
        eratosthenes(n)


print(f'простое число под номером {n} = {eratosthenes(n)} (с использованием решетки эрастофена)')
print(f'время затраченное на 1000 вызовов без использования решетки эрастофена - {timeit.timeit(f"eratosthenes({n})", globals=globals(), number=1000)}')
print('1000 вызовов для просмотра пролайфера')
cProfile.run('main_eratosthenes()')
# простое число под номером 15 = 47 (с использованием решетки эрастофена)
# время затраченное на 1000 вызовов без использования решетки эрастофена - 0.05802850000000004
# 1000 вызовов для просмотра пролайфера
#          97004 function calls in 0.069 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.069    0.069 <string>:1(<module>)
#      1000    0.035    0.000    0.069    0.000 l4_t2.py:63(eratosthenes)
#         1    0.000    0.000    0.069    0.069 l4_t2.py:79(main_eratosthenes)
#         1    0.000    0.000    0.069    0.069 {built-in method builtins.exec}
#     48000    0.032    0.000    0.032    0.000 {built-in method builtins.min}
#     48000    0.003    0.000    0.003    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


def eratosthenes2(number):
    # вариант решето эрастофена, но не полный алгоритм + использование затратной операции pop
    numbers_list = [i for i in range(2, number * number)]
    for i in numbers_list:
        for j in numbers_list:
            if j % i == 0 and i != j:
                numbers_list.pop(numbers_list.index(j))
    return numbers_list[number - 1]


def main_eratosthenes2():
    for _ in range(1000):
        eratosthenes2(n)


print(f'простое число под номером {n} = {eratosthenes2(n)} (с использованием решетки эрастофена)')
print(f'время затраченное на 1000 вызовов без использования решетки эрастофена - {timeit.timeit(f"eratosthenes2({n})", globals=globals(), number=1000)}')
print('1000 вызовов для просмотра пролайфера')
cProfile.run('main_eratosthenes2()')
# простое число под номером 15 = 47 (с использованием решетки эрастофена)
# время затраченное на 1000 вызовов без использования решетки эрастофена - 0.17595340000000004
# 1000 вызовов для просмотра пролайфера
#          352004 function calls in 0.219 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.218    0.218 <string>:1(<module>)
#      1000    0.118    0.000    0.218    0.000 l4_t2.py:101(eratosthenes2)
#      1000    0.004    0.000    0.004    0.000 l4_t2.py:103(<listcomp>)
#         1    0.000    0.000    0.218    0.218 l4_t2.py:111(main_eratosthenes2)
#         1    0.000    0.000    0.219    0.219 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    175000    0.078    0.000    0.078    0.000 {method 'index' of 'list' objects}
#    175000    0.019    0.000    0.019    0.000 {method 'pop' of 'list' objects}