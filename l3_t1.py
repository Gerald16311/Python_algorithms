# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

numbers_list = [n for n in range(2, 100)]
numbers_dict = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

for i in numbers_list:
    for y in range(2, 10):
        if i % y == 0:
            numbers_dict[y] += 1
        else:
            pass

print('В диапазоне натуральных чисел от 2 до 99 получился такой результат')
for key, value in numbers_dict.items():
    print(f'кратно {key} - получилось {value} чисел')
