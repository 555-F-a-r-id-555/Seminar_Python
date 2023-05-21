# № 47
# Ввод:
# values = [1, 23, 42, ‘asdfg’]
# transformed_values = list(map(trasformation, values))
# if values == transformed_values:
#     print(‘ok’)
# else:
#     print(‘fail’)
# Вывод:
# ok

# transfotmation = lambda x: x

values = [1, 23, 42, 'asdfg']
transformed_values = list(map(lambda x: x, values))
if values == transformed_values:
    print('ok')
else:
    print('fail')

# Задача №49. Решение в группах
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# ﬁnd_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую  площадь. Гарантируется, что самая далекая
# планета ровно одна

# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10

# find_farthest_orbit(list_of_orbits)

import math

from functools import reduce


def find_farthest_orbit(list_of_orbits):
    # print(find_farthest_orbit := max(list(map(lambda a: math.pi * a[0] * a[1], list_of_orbits))))
    find_orbit = filter(lambda x: x[0] != x[1], list_of_orbits)
    find_farthest_orbits = reduce(lambda a, b: a if math.pi * a[0] * a[1] > math.pi * b[0] * b[1] else b, find_orbit)
    return find_farthest_orbits


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))


def find_farthest_orbit_2(list_of_orbits):
    return max(list_of_orbits, key=lambda x: (x[0] != x[1]) * x[0] * x[1])


print(*find_farthest_orbit_2(orbits))

l = [1, 2, 3, 4, 5]
print(sorted(orbits, key=lambda x: x[0] > x[1]))

print(sorted(l, key=lambda x: x % 2 == 0))

# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.

# Ввод:
# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)
#
# Вывод:
# same

# same_by(lambda x: x % 2, values):
#     filter()

values = [0, 2, 10, 6]
print((reduce(lambda x, y: x % 2 == 0 and y % 2 == 0, values)))


def same_by(characteristic, objects):
    if reduce(lambda x, y: characteristic(x) == characteristic(y), objects):
        print('same')
    else:
        print('different')


characteristics = lambda x: x % 2
values = [0, 2, 10, 6]
same_by(characteristics, values)


def same_by(characteristic, objects):
    if len(list(filter(lambda x: characteristic(x) == 0, objects))) == len(objects):
        print('same')
    else:
        print('different')


def func(x):
    return x % 2


characteristics = lambda x: x % 2
values = [0, 2, 10, 6]
same_by(func, values)


# ---------------------------------------------


def test(x):
    return lambda n: n % x == 0


fun = test(2)
print(func(8))


def test2(x):
    def test3(n):
        return n % x == 0

    return test3


fun2 = test2(2)
print(fun2(8))

some_list = [1, 2, 3, 45]
other_list = ['a', 'b', 'c', 'd']

print(tuple(zip(other_list, some_list)))
dict_1 = dict(zip(other_list, some_list))
print(*dict(zip(other_list, some_list)))


def f(a, b, c, d):
    return a + b + c + d


print(f(**dict_1))


def f_2(**kwargs):
    print(kwargs)


f_2(a=4, b=7, c=5)


def f_3(*args):
    return sum(args)


print(f_3(1, 2, 3, 4, 5))

from collections import defaultdict

d = defaultdict(int)
d['a'] += 1
print(d)

