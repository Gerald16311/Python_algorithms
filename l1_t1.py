# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

input_number = int(input('Введите любое 3х значное число = '))
if 99 < input_number < 1001:
    a = input_number // 100
    input_number -= a * 100
    b = input_number // 10
    input_number -= b * 10
    print(f"сумма чисел {a+b+input_number}")
    print(f"произведение чисел {a*b*input_number}")
else:
    print ('Введено не верное число')
