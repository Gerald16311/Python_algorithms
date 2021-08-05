# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
# уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти. Примечание:
# Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи. Результаты
# анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность вашей ОС.


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


# 2 вариант через срез
def slised(n):
    result = n[::-1]
    return result


def main_slised():
    for _ in range(1000):
        slised(number)


print(f"2 Результат (срез) - {slised(number)}")


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
