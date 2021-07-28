# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
# Результаты анализа сохранить в виде комментариев в файле с кодом.

n = 15
# print(numbers_list)


# Без использования «Решета Эратосфена»;
def no_eratosthenes(n):
    numbers_list = [i for i in range(2, n + 1)]
    result_list = []
    for i in numbers_list:
        count = 0
        for y in range(2, numbers_list.index(i) - 1):
            # print(f"i = {i}, y = {y}")
            if i % y == 0:
                count += 1
            else:
                pass
        if count == 1:
            result_list.append(i)
        else:
            result_list.append(0)

    return result_list


print(no_eratosthenes(n))


# Используя алгоритм «Решето Эратосфена»
def eratosthenes(n):
    a = []
    b = []
    if n < 4:
        return
    for i in range(2, n + 1, 1):
        a.append(i)
    while a:
        for i in a[1:]:
            if i % a[0] == 0:
                b.append(i)
                a.remove(i)
        a = a[1:]
    for i in a:
        print(i, end=" ")


eratosthenes(n)
