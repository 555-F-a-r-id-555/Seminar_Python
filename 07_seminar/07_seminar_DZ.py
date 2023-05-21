# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод:
# пара-ра-рам рам-пам-папам па-ра-па-дам
# Вывод:    Парам пам-пам

# 1 new version_1
def winnie(lyrics):
    vowels = ('а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы')
    lyrics = lyrics.split()
    result = list(map(lambda x: sum(list(map(lambda i: x.count(i), vowels))), lyrics))
    print('Парам пам-пам' if len(set(result)) == 1 else 'Пам парам')


winnie('пара-ру-рам рам-пам-папам па-ра-па-дам')

# 2 new version_2
from functools import reduce


def winnie_2_0(lyrics):
    vowels = ('а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы')
    lyrics = lyrics.split()
    result = reduce(lambda x, y: x if sum(list(map(lambda i: x.count(i), vowels))) == sum(
        list(map(lambda i: y.count(i), vowels))) else "NO", lyrics)
    print("Парам пам-пам" if result != "NO" else 'Пам парам')


winnie_2_0('пара-ру-рам рам-пам-папам па-ра-па-дам')


# 3 - вариант
# def vinny_1(lyrics):
#     vowels = ('а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы')
#     count_1 = 0
#
#     lyrics = lyrics.split()
#     for j, x in enumerate(lyrics):
#         count_2 = count_1
#         count_1 = 0
#         for i in x:
#             if i in vowels:
#                 count_1 += 1
#         if count_2 != count_1 and j > 0:
#             print('Пам парам')
#             break
#     else:
#         print('Парам пам-пам')
#
#
# vinny_1('пара-ра-рам рам-пам-папам па-ра-па-дам')
# vinny_1('пар-ра-рам рам-пам-папам па-ра-па-дам')


# 4 - вариант
# def vinny_2(lytrics):
#     lytrics = lytrics.split()
#     vowels = ('а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы')
#     for j, elem in enumerate(lytrics):
#         count_2 = sum([lytrics[j].count(i) for i in vowels if i in lytrics[j]])
#         if j > 0 and temp != count_2:
#             print('Пам парам')
#             break
#         temp = count_2
#
#     else:
#         print('Парам пам-пам')
#
#
# vinny_2('пара-ру-рам рам-пам-папам па-ра-па-дам')
# vinny_2('пара-ру-рам рам-пам-папм па-ра-па-дам')


# Задача 36:  Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.
# Ввод:
# print_operation_table(lambda x, y: x * y)
# Вывод:
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

# 1 new version
def print_operation_table(operation, num_rows, num_columns):
    row = range(1, num_rows + 1)
    column = range(1, num_columns + 1)
    table = list(map(lambda x: list(map(lambda y: operation(x, y), column)), row))
    return table


operator = lambda x, y: x * y
[print(*x) for x in print_operation_table(operator, 6, 6)]


# 2 - old Версия
def print_operation_table(operation, num_rows, num_columns):
    for x in range(1, num_rows + 1):
        print(*list(map(lambda y: x * y, range(1, num_columns + 1))))


operator_1 = lambda x, y: x * y
print_operation_table(operator_1, 6, 6)

# 2 - New version

# def print_operation_table_new(operation, num_rows, num_columns):
#     row = range(1, num_rows + 1)
#     column = range(1, num_columns + 1)
#     table = list(map(lambda x: list(map(lambda y: operation(x, y), row)), column))
#     [print(*i) for i in table]
#
#
# operator_2 = lambda x, y: x * y
# print_operation_table_new(operator_2, 6, 6)
