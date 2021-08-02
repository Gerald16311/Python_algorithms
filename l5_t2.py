# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’,
# ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’,
# ‘E’]. Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля collections
first_number_16 = [i for i in input("Введите первое шестнадцатиричное число - ")]
second_number_16 = [i for i in input("Введите второе шестнадцатиричное число - ")]

first_number_10 = int("".join(first_number_16), base=16)
second_number_10 = int("".join(second_number_16), base=16)

numbers_sum_10 = first_number_10 + second_number_10
numbers_mult_10 = first_number_10 * second_number_10

result_sum_16 = []
result_mult_16 = []

for i in str(hex(numbers_sum_10)):
    result_sum_16.append(i.upper())
for i in str(hex(numbers_mult_10)):
    result_mult_16.append(i.upper())

result_sum_16 = result_sum_16[2:]
result_mult_16 = result_mult_16[2:]

print(f'Сумма 2х введенных 16ричных чисел ( 1 число - {first_number_16}, 2 число - {second_number_16}) '
      f'сумма = {result_sum_16}')
print(f'Произведение 2х введенных 16ричных чисел ( 1 число - {first_number_16}, 2 число - {second_number_16}) '
      f'произведение = {result_mult_16}')
