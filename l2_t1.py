# Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции
# вводятся пользователем. После выполнения вычисления программа не должна завершаться, а должна запрашивать новые
# данные для вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
# снова запрашивать знак операции. Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в
# качестве делителя.

first_number = 0
second_number = 0
operand = ""


def input_numbers():
    global first_number
    global second_number
    first_number = int(input("Введите первое число - "))
    second_number = int(input("Введите второе число - "))


while operand != 0:
    operand = input("Введите какую операцию вы хотите сделать над числами (0 - выход) - ")
    if operand == '+':
        input_numbers()
        print(f"Сумма - {first_number + second_number}")
    elif operand == '-':
        input_numbers()
        print(f"Разница - {first_number - second_number}")
    elif operand == '*':
        input_numbers()
        print(f"Произведение - {first_number * second_number}")
    elif operand == '/':
        input_numbers()
        if second_number != 0:
            print(f"Разделение - {first_number / second_number}")
        else:
            print('На 0 делить нельзя')
            continue
    elif operand == "0":
        print('Выход')
        break
    else:
        print("Введен не верный символ операции")
