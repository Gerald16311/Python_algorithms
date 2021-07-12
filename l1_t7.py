# По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного
# из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным
# или равносторонним.
a, b, c = [int(i) for i in input("Введите длины трех отрезков = ").split()]


def triangl_type():
    if a == b or a == c or b == c:
        print("Треугольник равнобедренный")
    elif a == b == c:
        print("Треугольник равносторонний")
    else:
        print("Треугольник разносторонний")


distance_list = [a, b, c]
distance_list.sort(reverse=True)

if distance_list[0] == 0 or distance_list[1] == 0 or distance_list[2] == 0:
    print("Невозможен треугольник, если хотя бы 1 из сторон = 0")
elif (distance_list[1] + distance_list[2]) == distance_list[0]:
    print("Вырожденный треугольник (все вершины лежат на 1 линии)")
elif (distance_list[1] + distance_list[2]) > distance_list[0]:
    triangl_type()
else:
    print("Треугольник не возможен")
