# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’,
# ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’,
# ‘E’]. Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля collections
first_number = [i for i in input("Введите первое шестнадцатиричное число - ")]
second_number = [i for i in input("Введите второе шестнадцатиричное число - ")]
print(first_number)
print(second_number)

print(int("".join(first_number), base=16))
print(int("".join(second_number), base=16))
first_number_10 = int("".join(first_number), base=16)
second_number_10 = int("".join(second_number), base=16)

numbers_sum_10 = first_number_10 + second_number_10
numbers_mult_10 = first_number_10 * second_number_10

result_sum = []
result_mult = []

for i in str(hex(numbers_sum_10)):
    result_sum.append(i.upper())
for i in str(hex(numbers_mult_10)):
    result_mult.append(i.upper())

result_sum = result_sum[2:]
result_mult = result_mult[2:]

print(f'Сумма 2х введенных 16ричных чисел ( 1 число - {first_number}, 2 число - {second_number}) сумма = {result_sum}')
print(f'Произведение 2х введенных 16ричных чисел ( 1 число - {first_number}, 2 число - {second_number}) произведение = {result_mult}')